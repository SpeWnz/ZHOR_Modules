# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    import nicePrints as np
else:
    from . import nicePrints as np

# =============================================================================

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
                
                



    else:
        # da implementare per il futuro
        np.errorPrint("NON SONO STATI IMPLEMENTATI ALTRI TIPI")
        raise NotImplemented
        pass



# Converte una lista in una stringa
def listToString(inputList: list):
    output = ""
    for item in inputList:
        output += str(item)
    
    return output
