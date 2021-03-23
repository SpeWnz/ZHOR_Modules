from termcolor import colored, cprint

# ========================================================================================================================================================= 
# VARIABILI GLOBALI

# Nel file principale in cui è stato importato "nicePrints.py" si deve specificare se questa variabile
# deve essere True o False, in maniera tale che la funzione debugPrint sa se deve stampare un messaggio o no
DEBUG = False


# ========================================================================================================================================================= 


# stampa di debug
def debugPrint(message):
    if (DEBUG):
        print("[", end='')
        cprint("D", 'yellow', end='')
        print("]", message)


# stampa di informazione generica
def infoPrint(message):
    print("[", end='')
    cprint("I", 'green', end='')
    print("]", message)


# stampa di errore
def errorPrint(message):
    print("[", end='')
    cprint("E", 'red', end='')
    print("] " + message)
