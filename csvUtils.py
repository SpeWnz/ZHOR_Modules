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
import os
from datetime import datetime
import pandas as pd
import sqlite3

# =============================================================================



# ottiene un timestamp del tipo dd-mm-yyyy_hh-mm-ss
def getTimeStamp():
    np.warningPrint("csvUtils.getTimeStamp(): This method is deprecated, please use timestampsUtils.py instead.")
    currentDateTime = datetime.now()
    outStr = "{}-{}-{}_{}-{}-{}".format(
        currentDateTime.day,
        currentDateTime.month,
        currentDateTime.year,
        currentDateTime.hour,
        currentDateTime.minute,
        currentDateTime.second
    )
    return outStr



# input > dict
# output > string
# example: "aaa;bbb;ccc"
def parseCSVHeader(inputDict: dict,separator=';'):
    outStr = ""
    for key in inputDict:
        outStr += key + separator

    outStr = outStr[:-1]
    

    return outStr


# l'oggetto in input è un LOD se e solo se è una lista di dizionari
# ogni oggetto nella lista deve essere un dizionario
def isLOD(inputObject):
    if (type(inputObject) != list):
        return False

    else:

        for item in inputObject:
            if (type(item) == dict):
                pass
            else:
                return False

    return True


# True se la grandezza in byte è > 0
# False altrimenti
def fileIsEmpty(inputFilePath):
    
    # se non esiste il file
    if(not os.path.isfile(inputFilePath)):
        return False
    
    size = os.path.getsize(inputFilePath)
    if size > 0:
        #print(inputFilePath,"non è vuoto")
        return False
    else:
        return True


# rimuove righe duplicate 
def deleteDuplicateRows_inCSV(csvFilePath):
    lines = fm.fileToSimpleList(csvFilePath)
    lines = list(dict.fromkeys(lines))

    fm.listToFile(lines, csvFilePath)

# rimuove gli header duplicati
def deleteDuplicateHeaders_inCSV(csvFilePath):
    lines = fm.fileToSimpleList(csvFilePath)
    header = lines[0]

    newFileLines = [header]

    for line in lines:
        if line == header:
            pass
        else:
            newFileLines.append(line)


    fm.listToFile(newFileLines, csvFilePath)


# lod = list of dicts
def lod2CSV(jsonObject, lod: list, csvPath: str,externalKey=None):
    
    if len(lod) < 1:
        return
        

    #header con le chiavi
    csvHeader = parseCSVHeader(lod[0])

    if(externalKey is None):
        csvLines = [csvHeader]
    else:
        csvLines = [csvHeader + ";" + externalKey + "_EXT_KEY"]

    for DICT in lod:
        line = ""

        for key in DICT:
            if (type(DICT[key]) is list):
                line += lu.concatenate_elements(DICT[key],delimiter=' ') + ";" 
            elif (type(DICT[key]) is str):
                line += '"{}";'.format(DICT[key])
            else:
                line += str(DICT[key]) + ";"


        if (externalKey is None):
            line = line[:-1]
        else:
            line += str(jsonObject[externalKey])

        csvLines.append(line)

    
    fm.listToFile(csvLines,csvPath)



# lod = list of dicts
def lod2CSV_v2(lod: list, csvPath: str,externalKey_name=None, externalKey_value=None,mode='w',insertHeader=True,subLOD_folder=".",subLOD_suffix="",separator=';'):
    
    if(len(lod) < 1):
        return

    def stringSanification(inputString: str):
        s = inputString.replace('"','\\"')
        return s



    #header con le chiavi
    #print(lod)
    #input()
    try:
        csvHeader = parseCSVHeader(lod[0],separator=separator)
    except Exception as e:
        np.errorPrint("Errore su csvHeader: Eccezione: {}".format(str(e)))
        print("Contenuto lod:",lod)
        return

    # GESTIONE CSV HEADER ==========================================================

    if(mode == 'a') and (fileIsEmpty(csvPath) is False):
        pass
        #insertHeader = False

    if(insertHeader):
        if(externalKey_name is None):
            csvLines = [csvHeader]
        else:
            csvLines = [csvHeader + separator + externalKey_name + "_EXT_KEY"]
    else:
        csvLines = []

    # ==============================================================================

    for DICT in lod:
        #print("DICT",DICT)
        #print("lod:",lod)
        #input()
        line = ""

        
        for key in DICT:
            #os.system("clear")
            #print("==================================")
            #print("Key --->",key,"\n\n")
            #print("DICT --->",DICT,"\n\n")
            #print("DICT[key] --->",DICT[key])
            #input()
            
            
            try:
                if(isLOD(DICT[key])):
                    #print("subLOD",DICT[key])
                    #print("subLOD KEY:",key)
                    #input()
                    subLOD_csvPath = subLOD_folder + "/" + str(key) + subLOD_suffix + ".csv"
                    
                    # per default, la chiave esterna dei sub-lod è la prima chiave che trova nel dizionario del lod
                    # questo perchè, si presume, la prima chiave è sempre un ID univoco che identifica il livello superiore
                    sublodExtKey = list(DICT.keys())[0] 
                    sublodExtValue = DICT[sublodExtKey]
                    #print("sublodExtKey ---> ",sublodExtKey)
                    lod2CSV_v2(lod=DICT[key], csvPath=subLOD_csvPath,externalKey_name=sublodExtKey,externalKey_value=sublodExtValue,mode='a',separator=separator)
                else:

                    if (type(DICT[key]) is list):
                        line += lu.concatenate_elements(DICT[key],delimiter=' ') + separator
                    elif (type(DICT[key]) is str):
                        val = stringSanification(DICT[key])
                        line += '"{}"{}'.format(val,separator)
                    else:
                        line += str(DICT[key]) + separator

            except Exception as e:
                print("==================================")
                np.errorPrint("Couldn't parse data for this object")
                print("Dictionary: ",DICT)
                print("Key: ",key)
                print("Exception:",e)
                #print("Value: ",DICT[key])
                print("==================================")
                #input()



        if (externalKey_name is None):
            line = line[:-1]
        else:
            line += str(externalKey_value)

        csvLines.append(line)

    
    fm.listToFile(csvLines,csvPath,mode=mode)

# takes a string, a charset, and a replacing character as input.
# the charset is just a string with characters you want to replace.
# the "replacing character" is that character you are replacing the charset with.
# for example: if the string is "hello123", the charset is "ho123", and the replacingcharacter is "_"
# then the resulting string will be "_"
def stringSanification(inputString: str, charset: str, replacingCharacter: str):
    for char in inputString:
        if char in charset:
            inputString = inputString.replace(char,replacingCharacter)
            
    return inputString

# generic implementation: converts a csv file into a sqlite db file
def csv2db(csvFile: str, dbFile: str, tableName: str, separator=',',overwrite=False):

    # insert more blacklist characters as they are found
    charactersBlacklist = ':.-+*/#?!,;' 

    # should we append data to the db or create a new db?
    if overwrite and fm.fileExists(dbFile):
        os.remove(dbFile)

    # curry function for datbase types
    def get_sqlite_type(series):
        if pd.api.types.is_integer_dtype(series):
            return 'INTEGER'
        elif pd.api.types.is_float_dtype(series):
            return 'REAL'
        else:
            return 'TEXT'

    # dataframe construction and values stripping
    df = pd.read_csv(csvFile,sep=separator)
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # apply further string sanifications for the csv header only
    df.columns = df.columns.map(lambda x: x.replace(' ','_'))
    df.columns = df.columns.map(lambda x: stringSanification(x,charactersBlacklist,''))

    # apply sanification rules to table name as well
    tableName = stringSanification(tableName,charactersBlacklist,'')

    # create SQLite database and connect to it
    conn = sqlite3.connect(dbFile)
    cursor = conn.cursor()

    # create the table based on CSV columns and types
    columns = df.columns.tolist()
    column_defs = []    

    # determine variable types for the database
    for col in columns:
        column_type = get_sqlite_type(df[col])
        column_defs.append(f"{col} {column_type}")

    # create the table
    create_table_query = "CREATE TABLE IF NOT EXISTS {} ({});".format(tableName,', '.join(column_defs))
    cursor.execute(create_table_query)

    # pour data into the table
    for row in df.itertuples(index=False, name=None):
        com = "INSERT INTO {} ({}) VALUES ({})".format(
            tableName,
            ', '.join(columns),
            ', '.join(['?'] * len(row))
        )
        cursor.execute(com, row)

    # Commit and close
    conn.commit()
    conn.close()