# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    import nicePrints as np
    import listUtils as lu
else:
    from . import nicePrints as np
    from . import listUtils as lu

# =============================================================================

# controlla la presenza di argomenti mutualmente esclusivi (non possono essere presenti tutti insieme)
# input: sys.argv, lista di argomenti mutualmente esclusivi
# esempio: checkMutExArgs(sys.argv, ["--argument1","--argument3","-a"])
# return True, contiene mutex args
# return False, altrimenti
def checkMutExArgs(sysArgv_arguments: list, mutuallyExclusiveArguments: list,errorMessage="Mutually exclusive arguments: "):
    mutexCounter = 0

    mutexArgs = []
    for item in mutuallyExclusiveArguments:
        if item in sysArgv_arguments:
            mutexCounter += 1
            mutexArgs.append(item)
    
    if mutexCounter > 1:
        np.errorPrint(errorMessage + lu.listToString(mutexArgs,' '))
        return True

    return False


# controlla la presenza di argomenti mutualmente inclusivi (devono essere presenti tutti)
# input: sys.argv, lista di argomenti mutualmente inclusivi
# esempio: checkMutExArgs(sys.argv, ["--argument1","--argument3","-a"])
# return True, contiene mutinc args
# return False, altrimenti
def checkMutIncArgs(sysArgv_arguments: list, mutuallyInclusiveArguments: list,errorMessage="Mutually inclusive arguments: "):
    
    for item in mutuallyInclusiveArguments:
        if item not in sysArgv_arguments:
            np.errorPrint(errorMessage + lu.listToString(mutuallyInclusiveArguments,' '))
            return True

    return False

