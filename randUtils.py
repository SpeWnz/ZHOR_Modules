import random
import string
import sys
import os

# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    import nicePrints
    #print("POTATOOOOOOOOOOOOOOOOOO")
else:
    #print("CARROTTTTTTTTTTTTTTTTTT")
    from . import nicePrints

# =============================================================================

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

def randomStringArray(arrayLen: int, minStrLen: int, maxStrLen: int, lowers=True,uppers=True,alphabetOnly=True):
    outputArray = []
    pass


def randomIntegerArray(lb, ub, d):
    a = []
    for i in range(lb, ub):
        a.append(i)

    r = []
    for index in range(d):
        r.append(random.choice(a))
    return r

def extractRandomNumber(lb, ub):
    a = []
    for i in range(lb, ub):
        a.append(i)
    return random.choice(a)