# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    import nicePrints as np
else:
    from . import nicePrints as np

# =============================================================================

def quickSort(inputList: list):
    return partition(inputList)

def partition(inputList: list):
    length = len(inputList)

    if length == 0:
        return

    if length == 1:
        return inputList

    lessOrEqual = []
    moreThan = []
    pivotIndex = int(length/2)

    for i in range(0,length):
        if inputList[i] <= inputList[pivotIndex]:
            lessOrEqual.append(inputList[i])
        else:
            moreThan.append(inputList[i])

    print("lessOrEqual:", lessOrEqual)
    print("pivot:", inputList[pivotIndex])
    print("moreThan:",moreThan)
    input()


    return partition(lessOrEqual) + partition(moreThan)
    
def bubbleSort(A: list):
    sorted = False

    while(not sorted):
        sorted = True
        for i in range(0,len(A)):
            if (i+1 < len(A)) and (A[i] > A[i+1]):
                #swap
                app = A[i]
                A[i] = A[i+1]
                A[i+1] = app
                sorted = False

    return A

# ============ MAIN

a = [7,2,4,1,6,8,10,9]
print(bubbleSort(a))

