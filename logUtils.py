# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    import nicePrints as np
else:
    from . import nicePrints as np


import threading

# =============================================================================


LOG_PATH = 'log.log'    # default log path

# specifically logs exceptions and traceback.
# usage: logu.logException(traceback,e,fileName='path here')
# remember to "import traceback" in your projeect
def logException(tracebackObject,exceptionObject,fileName=LOG_PATH,lock=None,stdout=True):
    
    if lock is None:
        pass
    else:
        lock.acquire()
    
    if stdout:
        np.errorPrint(f'The following exception occurred: {exceptionObject}. Check the traceback in the log.')

    msg = f'[EXCEPTION] {exceptionObject}. Traceback: {tracebackObject.format_exc()} \n'
    open(fileName,'a').write(msg)
    
    if lock is None:
        pass
    else:
        lock.release()

def logError(message: str,fileName=LOG_PATH, lock=None,stdout=True):
    
    if lock is None:
        pass
    else:
        lock.acquire()
    
    if stdout:
        np.errorPrint(message)

    open(fileName,'a').write("[ERROR] " + message + "\n")
    
    if lock is None:
        pass
    else:
        lock.release()

def logDebug(message: str,fileName=LOG_PATH, lock=None,stdout=True):
    
    if lock is None:
        pass
    else:
        lock.acquire()
    
    if stdout:
        np.debugPrint(message)

    open(fileName,'a').write("[DEBUG] " + message + "\n")
    
    if lock is None:
        pass
    else:
        lock.release()

def logInfo(message: str,fileName=LOG_PATH, lock=None,stdout=True):
    
    if lock is None:
        pass
    else:
        lock.acquire()
    
    if stdout:
        np.infoPrint(message)
        
    open(fileName,'a').write("[INFO] " + message + "\n")
    
    if lock is None:
        pass
    else:
        lock.release()