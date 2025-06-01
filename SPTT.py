# stuff for SPTT
# https://github.com/SpeWnz/SPTT

# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    import nicePrints as np
    import fileManager as fm
    import listUtils as lu
    import osUtils as osu
else:
    from . import nicePrints as np
    from . import fileManager as fm
    from . import listUtils as lu
    from . import osUtils as osu


# OTHER MODULES
import sqlite3
import threading

# =============================================================================


class TupleCacher:

    CACHE_DB = None
    TABLE_NAME = None

    _inMemoryTuples = []                        # list of tuples
    _inMemoryTuples_limit   = 1000              # how many tuples can you have in memory before dumping to disk
    _inMemoryTuples_lock    = threading.Lock()
    _columnNames = None
    _columnTypes = None

    _databaseCursorLock     = threading.Lock()  # lock used for both reading and writing operations


    def __init__(self,dbPath: str,columnNames: list,tableName='tuples',columnTypes=None):
        self.CACHE_DB = dbPath
        self.TABLE_NAME = tableName
        self._columnNames = columnNames

        # by default, all columns are text
        if columnTypes == None:
            columnTypes = []
            for i in range(0,len(columnNames)):
                columnTypes.append('TEXT')

        # the final column is always text (for the result)
        self._columnTypes = columnTypes + ['TEXT']

        conn = sqlite3.connect(dbPath,check_same_thread=False)
        cursor = conn.cursor()

        sql = f"CREATE TABLE IF NOT EXISTS {tableName}( "
        for i in range(0,len(columnNames)):
            sql += f"{columnNames[i]} {columnTypes[i]},"

        # result column (where we will store either "success" or "fail")
        sql += " result TEXT)"

        cursor.execute(sql)
        
        conn.commit()
        conn.close()



    # transforms into blob string, e.g. X'........'
    def __getBlob(self, inputValue):
        return f"X'{inputValue.encode("utf-8").hex()}'"

    # takes the list of tuples and converts them into rows of sql "values" statements
    # to feed into the insert sql, e.g:
    # (val1, val2, val3), (val1, val2, val3)
    def getFormattedValues(self):
        output = ""
        for iMT in self._inMemoryTuples:
            
            _toAppend = '('
            for i in range(0,len(iMT)):
                
                # handle text
                if self._columnTypes[i] == "TEXT":
                    _toAppend += f'"{iMT[i]}",'

                # handle blob
                if self._columnTypes[i] == "BLOB":
                    _toAppend += f'{self.__getBlob(iMT[i])},'


            _toAppend = _toAppend[:-1] + "),"
            output += _toAppend
        
        return output[:-1]


    # handles insertion of tuples.
    # dumps to db every X tuples, where X is the limit of the amount of tuples that
    # can be stored in memory.
    # by default it is 1000
    def __insertStatus(self,tuple_:tuple,status:str):        
        self._inMemoryTuples_lock.acquire()

        _toAppend = tuple(list(tuple_) + [status])
        self._inMemoryTuples.append(_toAppend)

        if len(self._inMemoryTuples) >= self._inMemoryTuples_limit:
            self.dumpToDB()
            self._inMemoryTuples = []

        self._inMemoryTuples_lock.release()

    # when the in-memory list is full, dump to disk
    def dumpToDB(self):

        # edge case: there may be no tuples at all.
        # example, testing against a target that yielded an exception in 100% of cases.
        # in this case, no tuples would be stored, so calling dumpToDB() would cause an
        # exception
        if len(self._inMemoryTuples) == 0:
            return


        self._databaseCursorLock.acquire()

        sql = "INSERT INTO {} ({}) VALUES {}".format(
            self.TABLE_NAME,
            ', '.join(self._columnNames + ['result']),
            self.getFormattedValues()
        )

        writeConn = sqlite3.connect(self.CACHE_DB)
        writeCursor = writeConn.cursor()
        writeCursor.execute(sql)

        writeConn.commit()
        writeConn.close()

        self._databaseCursorLock.release()


    def insertSuccess(self, tuple_:tuple):
        self.__insertStatus(tuple_,'success')

    def insertFail(self, tuple_:tuple):
        self.__insertStatus(tuple_,'fail')

    # reads from the db. If the tuple exists, return true. False otherwise
    def tupleExists(self,tuple_:tuple):
        
        where_clause = ' AND '.join([f"{col} = ?" for col in self._columnNames])

        sql = f"SELECT 1 FROM {self.TABLE_NAME} WHERE {where_clause} LIMIT 1"

        self._databaseCursorLock.acquire()

        readConn = sqlite3.connect(self.CACHE_DB)
        readCursor = readConn.cursor()
        readCursor.execute(sql,self._adjustTupleForQuery(tuple_))

        result = readCursor.fetchall()
        readConn.close()
        
        self._databaseCursorLock.release()

        if (len(result) == 0):
            return False
        
        return True
    
    # takes a tuple as input and adjust it based on the type of its column.
    # for example, if we have (TEXT,TEXT,BLOB)
    # then the third field of the tuple must be cast to hex
    def _adjustTupleForQuery(self,tuple_:tuple):
        newTuple = []

        for i in range(0,len(tuple_)):
            if self._columnTypes[i] == 'BLOB':
                newTuple.append(tuple_[i].encode('utf-8'))            
            else:
                newTuple.append(tuple_[i])

        return tuple(newTuple)

# 10000000 lines can be considered safe
# very large wordlists can cause python scripts to crash
def safeWordlistSize(wordlistPath: str):
    if osu.countLines(wordlistPath) <= 10000000:
        return True
    
    return False