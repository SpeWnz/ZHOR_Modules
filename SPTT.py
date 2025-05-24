# stuff for SPTT
# https://github.com/SpeWnz/SPTT

# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    import nicePrints as np
    import fileManager as fm
    import listUtils as lu
else:
    from . import nicePrints as np
    from . import fileManager as fm
    from . import listUtils as lu


# OTHER MODULES
import sqlite3

# =============================================================================


class TupleCacher:

    CACHE_DB = None
    TABLE_NAME = None

    _columnNames = None
    _conn = None
    _cursor = None


    def __init__(self,dbPath: str,columnNames: list,tableName='tuples'):
        self.CACHE_DB = dbPath
        self.TABLE_NAME = tableName
        self._columnNames = columnNames
        conn = sqlite3.connect(dbPath)
        cursor = conn.cursor()

        sql = f"CREATE TABLE IF NOT EXISTS {tableName}( "
        for c in columnNames:
            sql += f"{c} TEXT,"

        # result column (where we will store either "success" or "fail")
        sql += " result TEXT)"

        cursor.execute(sql)
        
        conn.commit()
        conn.close()

    # initializes the connection, the conn object, and cursor object
    def connectDB(self):
        self._conn = sqlite3.connect(self.CACHE_DB)
        self._cursor = self._conn.cursor()

    # closes and commit
    def disconnectDB(self):
        self._conn.commit()
        self._conn.close()


    def __insertStatus(self,tuple_:tuple,status:str):
        sql = "INSERT INTO {} ({}) VALUES ({})".format(
            self.TABLE_NAME,
            ', '.join(self._columnNames + ['result']),
            ', '.join(['?'] * (len(tuple_) + 1))
        )

        values = []
        for item in tuple_:
            values.append(item)

        values.append(status)

        self._cursor.execute(sql,values)

    def insertSuccess(self, tuple_:tuple):
        self.__insertStatus(tuple_,'success')

    def insertFail(self, tuple_:tuple):
        self.__insertStatus(tuple_,'fail')

    def tupleExists(self,tuple_:tuple):
        sql = f"SELECT * FROM {self.TABLE_NAME} WHERE "

        for item in self._columnNames:
            sql += f"{item} = ? AND "
        
        # remove the final " AND "
        sql = sql[:-5]
        self._cursor.execute(sql,tuple_)
        result = self._cursor.fetchall()

        if (len(result) == 0):
            return False
        
        return True