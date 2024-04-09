from termcolor import colored, cprint
import platform


#fix per windows
if("Windows" in platform.system()):
    import colorama
    colorama.init()

# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    pass
else:
    pass


# ========================================================================================================================================================= 
# VARIABILI GLOBALI

# Nel file principale in cui è stato importato "nicePrints.py" si deve specificare se questa variabile
# deve essere True o False, in maniera tale che la funzione debugPrint sa se deve stampare un messaggio o no
DEBUG = False

# lock utilizzato per i messaggi di stampa di nicePrints. Per default è vuoto, va impostato quando crei un nuovo
# script. Ad es: 
# PRINT_LOCK = threading.Lock()
# Per default quindi nicePrints non è auto-bloccante. Devi esplicitamente specificare che vuoi un thread lock
PRINT_LOCK = None

#Tipo di tag del messaggio:
#   0: [I] [E] [D] [?]
#   1: [INFO] [ERROR] [DEBUG] [QUESTION]
TAG_TYPE = 0

# ========================================================================================================================================================= 



# stampa di debug
def debugPrint(message,lock=PRINT_LOCK):
    if lock is None:
        pass
    else:
        lock.acquire()

    if (DEBUG):
        print("[", end='')
        if(TAG_TYPE == 0):
            cprint("D", 'yellow', end='')
        if(TAG_TYPE == 1):
            cprint("DEBUG", 'yellow', end='')
        print("]", message)

    if lock is None:
        pass
    else:
        lock.release()


# stampa di informazione generica
def infoPrint(message,lock=PRINT_LOCK):
    if lock is None:
        pass
    else:
        lock.acquire()

    print("[", end='')
    if(TAG_TYPE == 0):
        cprint("I", 'green', end='')
    if(TAG_TYPE == 1):
        cprint("INFO", 'green', end='')
    print("]", message)

    if lock is None:
        pass
    else:
        lock.release()


# stampa di errore
def errorPrint(message,lock=PRINT_LOCK):

    if lock is None:
        pass
    else:
        lock.acquire()

    print("[", end='')
    if(TAG_TYPE == 0):
        cprint("E", 'red', end='')
    if(TAG_TYPE == 1):
        cprint("ERROR", 'red', end='')
    print("] " + message)

    if lock is None:
        pass
    else:
        lock.release()

# stampa di una domanda / prompt
def questionPrint(message,lock=PRINT_LOCK):

    if lock is None:
        pass
    else:
        lock.acquire()

    print("[", end='')
    if(TAG_TYPE == 0):
        cprint("?", 'cyan', end='')
    if(TAG_TYPE == 1):
        cprint("QUESTION", 'cyan', end='')
    print("] " + message)

    if lock is None:
        pass
    else:
        lock.release()