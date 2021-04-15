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

#Tipo di tag del messaggio:
#   0: [I] [E] [D]
#   1: [INFO] [ERRORE] [DEBUG]
TAG_TYPE = 0

# ========================================================================================================================================================= 


# stampa di debug
def debugPrint(message):
    if (DEBUG):
        print("[", end='')
        if(TAG_TYPE == 0):
            cprint("D", 'yellow', end='')
        if(TAG_TYPE == 1):
            cprint("DEBUG", 'yellow', end='')
        print("]", message)


# stampa di informazione generica
def infoPrint(message):
    print("[", end='')
    if(TAG_TYPE == 0):
        cprint("I", 'green', end='')
    if(TAG_TYPE == 1):
        cprint("INFO", 'green', end='')
    print("]", message)


# stampa di errore
def errorPrint(message):
    print("[", end='')
    if(TAG_TYPE == 0):
        cprint("E", 'red', end='')
    if(TAG_TYPE == 1):
        cprint("ERRORE", 'red', end='')
    print("] " + message)
