# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    import nicePrints as np
else:
    from . import nicePrints as np


# =============================================================================


def logError(message: str,fileName="log.txt", lock=None):
    
    if lock is None:
        pass
    else:
        lock.acquire()
    
    np.errorPrint(message)
    open(fileName,'a').write("[ERROR] " + message + "\n")
    
    if lock is None:
        pass
    else:
        lock.release()

def logDebug(message: str,fileName="log.txt", lock=None):
    
    if lock is None:
        pass
    else:
        lock.acquire()
    
    np.debugPrint(message)
    open(fileName,'a').write("[DEBUG] " + message + "\n")
    
    if lock is None:
        pass
    else:
        lock.release()

def logInfo(message: str,fileName="log.txt", lock=None):
    
    if lock is None:
        pass
    else:
        lock.acquire()
    
    np.infoPrint(message)
    open(fileName,'a').write("[INFO] " + message + "\n")
    
    if lock is None:
        pass
    else:
        lock.release()
