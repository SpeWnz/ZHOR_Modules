# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    import nicePrints as np
else:
    from . import nicePrints as np

# =============================================================================

#np.DEBUG = True

# mostra in maniera carina e ordinata tutti gli elementi di una lista
def fancyPrint(inputList: list, printType=0):
    
    if (printType == 0):
        for i in range(0,len(inputList)):
            if(type(inputList[i]) is str):
                print(str(i+1) + ". \t",inputList[i])

            # se c'è una sottolista, stampa in questo modo:
            # 1. elem1 --- elem2 --- elem3 --- ... elemN
            # 2. elem1 --- elem2 --- elem3 --- ... elemN
            # 3. elem1 --- elem2 --- elem3 --- ... elemN
            if(type(inputList[i]) is list):
                print(str(i+1) + ". \t",end='')
                for item in inputList[i]:
                    print(item,"\t",end='')
                print("\n",end='')
    
            # se è una lista di tuple, stampa in questo modo:
            # 1. elem1 --- elem2 --- elem3 --- ... elemN
            # 2. elem1 --- elem2 --- elem3 --- ... elemN
            # 3. elem1 --- elem2 --- elem3 --- ... elemN
            if(type(inputList[i]) is tuple):
                print(str(i+1) + ". \t",end='')
                for item in inputList[i]:
                    print(item,"\t",end='')
                print("\n",end='')

    else:
        # da implementare per il futuro
        np.errorPrint("NON SONO STATI IMPLEMENTATI ALTRI TIPI")
        raise NotImplemented
        pass

# data in input una lista di due dimensioni (presumibilmente una tabella) 
# la stampa in maniera carina e ordinata
def tablePrint(inputTwoDimensionalList: list):  
    for row in inputTwoDimensionalList:
        for value in row:
            print(value,end=" ")

        print("\n",end="")

    

#concatena tutti gli elementi di una lista
def concatenate_elements(inputList: list, delimiter=None):
    if delimiter is None:
        return "".join(inputList)

    else:
        return delimiter.join(inputList)

# Converte una lista in una stringa
def listToString(inputList: list):
    return "".join(inputList)



# restituisce una lista di elementi che si trovano in "firstList" ma non in "secondList"
# checkSubstring: controlla la presenza o l'assenza anche sottoforma di sottostringa
# bidirectionalSubstring: fa il controllo "checkSubstring" in entrambe le direzioni, invece che solo da firstList a secondList
def uncommonElements(firstList: list, secondList: list, checkSubString=False, bidirectionalSubstring=False):

    def inListWSubstring(ITEM):
        for item in secondList:
            if ITEM in item:
                return True

            if bidirectionalSubstring:
                if item in ITEM:
                    return True

        return False

    outputList = []

    # opz 1: controllo senza checkSubstring
    if not checkSubString:
        for item in firstList:
            if item not in secondList:
                outputList.append(item)

        return outputList

    
    # opz 2: controllo con checkSubstring
    if checkSubString:
        for item in firstList:
            if not inListWSubstring(item):
                outputList.append(item)

        return outputList



# prende una lista e la divide in N pezzi.
# restituisce una lista di N sottoliste
# https://stackoverflow.com/questions/2130016/splitting-a-list-into-n-parts-of-approximately-equal-length
def splitList(inputList: list, count: int):
    k, m = divmod(len(inputList), count)
    return list(inputList[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(count))
