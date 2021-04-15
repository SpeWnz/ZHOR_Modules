import os

# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    pass
else:
    pass

# =============================================================================

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
def fileToSimpleList(inputFile):
    fileLines = open(inputFile, 'r').readlines()
    outputList = []

    for lines in fileLines:
        lines = lines.rstrip("\n")
        outputList.append(lines)

    return outputList