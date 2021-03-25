# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    pass
else:
    pass

# =============================================================================


# riversa le righe di un file in una lista (NON SEPARA I VALORI)
def fileToSimpleList(inputFile):
    fileLines = open(inputFile, 'r').readlines()
    outputList = []

    for lines in fileLines:
        lines = lines.rstrip("\n")
        outputList.append(lines)

    return outputList