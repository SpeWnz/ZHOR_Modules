import pathlib
import os
import hashlib

# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    pass
else:
    pass

# =============================================================================

DEFAULT_FILE_ENCODING = 'utf-8' # encoding di default usato per leggere e scrivere file


# dato un path di un file restituisce quel path senza estensione del file
def getFilePath_withoutExtention(filePath: str):
    return os.path.splitext(filePath)[0]

# dato un path di un file restituisce il nome del file senza estensione
def getFileName_withoutExtention(filePath: str):
    temp = getFilePath_withoutExtention(filePath)
    return temp.split("/")[-1]

# dato un path di un file restituisce l'estensione del file
def getFileExtention(filePath: str):
    return os.path.splitext(filePath)[1]


# riversa le righe di un file in una lista (NON SEPARA I VALORI)
def fileToSimpleList(inputFile,errors='ignore'):
    #https://stackoverflow.com/questions/49562499/how-to-fix-unicodedecodeerror-charmap-codec-cant-decode-byte-0x9d-in-posit
    fileLines = open(inputFile, 'r',encoding=DEFAULT_FILE_ENCODING,errors=errors).readlines()
    
    outputList = []

    for lines in fileLines:
        lines = lines.rstrip("\n")
        outputList.append(lines)

    return outputList

'''
Dato un file contenente sezioni, restituisce tanti dizionari quante sono le sezioni.
Ogni dizionario contiene come chiave il nome della sezione, e come valore una lista
che rappresenta tutte le righe di quella sezione.
Una sezione è definita da un cancelletto seguita da un "titolo", e contiene delle righe con dei dati
Esempio:
            # SEZIONE 1
            datoA
            datoB:valoreX
            datoC:valoreY
            # SEZIONE 2
            datoD:valoreZ
            datoE
            datoF:valoreK

Questo file sarà convertito nel seguente dizionario (NOTA: nel dare il nome alla chiave, gli spazi e i cancelletti
sono rimossi)
{'SEZIONE1': ["datoA","datoB:valoreX","datoC:valoreY"], 'SEZIONE2':["datoD:valoreZ","datoE","datoF:valoreK"]}
'''
def sectionedFileToDict(inputFile: str):
    outputDict = {}
    fileLines = fileToSimpleList(inputFile)

    #raccolgo la posizione di ogni cancelletto
    sectionIndexes = []
    for i in range(0,len(fileLines)):
        if("#" in fileLines[i]):
            sectionIndexes.append(i)

    # costruisco il dizionario
    for i in range(0,len(sectionIndexes)):
        keyName = str(fileLines[sectionIndexes[i]])
        keyName = keyName.replace("#","").replace(" ","")

        if((i+1) != len(sectionIndexes)):
            outputDict[keyName] = fileLines[(sectionIndexes[i] + 1):(sectionIndexes[i+1])]
        else:
            outputDict[keyName] = fileLines[(sectionIndexes[i] + 1):]

        
    return outputDict


# data una lista in input scrive un file con le righe della lista
def listToFile(inputList: list, fileName: str,mode='w'):
    with open(fileName, mode=mode,encoding=DEFAULT_FILE_ENCODING) as f:
        for item in inputList:
            f.write("%s\n" % item)


# returns true if a file exists, false if not
def fileExists(filePath: str):
    f = pathlib.Path(filePath)
    return f.is_file()

# returns true if a dir exists, false if not
def dirExists(dirPath: str):
    f = pathlib.Path(filePath)
    return f.is_dir()


# gets the MD5 hash of a file
def getMD5Sum(filePath: str):
    return hashlib.md5(open(filePath,'rb').read()).hexdigest()

# gets the SHA1 hash of a file
def getSHA1Sum(filePath: str):
    return hashlib.sha1(open(filePath,'rb').read()).hexdigest()


# using MD5,returns true if the file are identical, false if not
def compareMD5(filePath1:str, filePath2: str):
    return getMD5Sum(filePath1) == getMD5Sum(filePath2)

# using SHA1, returns true if the file are identical, false if not
def compareSHA1(filePath1:str, filePath2: str):
    return getSHA1Sum(filePath1) == getSHA1Sum(filePath2)
