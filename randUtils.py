import random
import string
import sys
import os

# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    import nicePrints
else:
    from . import nicePrints

# =============================================================================

# Restituisce un array casuale strutturato nel seguente modo
# [YYYYYEEEEESSSS]
# Il numero di Y, E, e S, è casuale
def randomYESarray():
    outputArray = []

    numOfY = extractRandomNumber(1,20)
    numOfE = extractRandomNumber(1,20)
    numOfS = extractRandomNumber(1,20)

    for i in range(0,numOfY):
        outputArray.append("Y")

    for i in range(0,numOfE):
        outputArray.append("E")

    for i in range(0,numOfS):
        outputArray.append("S")

    return outputArray

# Restituisce una stringa casuale
def randomString(stringLength: int,upperLetters=True,lowerLetters=True,numbers=True):
    
    if((upperLetters is False) and (lowerLetters is False) and (numbers is False)):
        nicePrints.errorPrint("Bisogna specificare almeno uno dei due campi da randomizzare.")
        raise Exception()
    
    choices = ""

    #aggiunge lettere maiuscole
    if(upperLetters):
        choices += string.ascii_uppercase

    #aggiunge lettere minuscole
    if(lowerLetters):
        choices += string.ascii_lowercase

    #aggiunge numeri
    if(numbers):
        choices += string.digits

    return ''.join(random.choices(choices, k=stringLength))

# Restituisce un array di stringhe casuali
def randomStringArray(arrayLen: int, minStrLen: int, maxStrLen: int, lowerLetters=True,upperLetters=True,numbers=True):
    outputArray = []

    if((upperLetters is False) and (lowerLetters is False) and (numbers is False)):
        nicePrints.errorPrint("Bisogna specificare almeno uno dei due campi da randomizzare.")
        raise Exception()

    for i in range(0,arrayLen):
        strToAppend = randomString(stringLength=extractRandomNumber(minStrLen,maxStrLen),lowerLetters=lowerLetters,upperLetters=upperLetters,numbers=numbers)
        outputArray.append(strToAppend)

    return outputArray

# Restituisce un array di numeri casuali
def randomIntegerArray(lb, ub, d):
    a = []
    for i in range(lb, ub):
        a.append(i)

    r = []
    for index in range(d):
        r.append(random.choice(a))
    return r

# Restituisce un numero casuale
def extractRandomNumber(lb, ub):
    a = []
    for i in range(lb, ub):
        a.append(i)
    return random.choice(a)