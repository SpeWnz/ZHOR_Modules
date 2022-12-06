# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    import nicePrints as np
    import listUtils as lu
else:
    from . import nicePrints as np
    from . import listUtils as lu

# =============================================================================

# controlla la presenza di argomenti mutualmente esclusivi
# input: sys.argv, lista di argomenti mutualmente esclusivi
# esempio: checkMutExArgs(sys.argv, ["--argument1","--argument3","-a"])
# return True, contiene mutex args
# return False, altrimenti
def checkMutExArgs(sysArgv_arguments: list, mutuallyExclusiveArguments: list):
    mutexCounter = 0

    mutexArgs = []
    for item in mutuallyExclusiveArguments:
        if item in sysArgv_arguments:
            mutexCounter += 1
            mutexArgs.append(item)
    
    if mutexCounter > 1:
        np.errorPrint("Mutually exclusive arguments: " + lu.listToString(mutexArgs,' '))
        return True

    return False

    

