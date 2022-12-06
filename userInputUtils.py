# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    import nicePrints as np
    import listUtils as lu
else:
    from . import nicePrints as np
    from . import listUtils as lu

# =============================================================================

# richiede all'utente di inserire una risposta da un set finito di scelte
# ad es: do you want to continue the operation? (y/n/m)
# impedisce di dare risposte errate
# message: il messaggio di input
# options: lista di opzioni
# errorMessage: messaggio di errore da stampare se l'input non è valido
# caseSensisitve: si spiega da solo
# defaultChoice: per default che risposta scegliere se l'utente sbaglia
# return della scelta dell'utente tra le varie disponibili
def promptOptions(message: str, options: list,errorMessage="Invalid choice. Please, retry.", caseSensitive=False,defaultChoice=None):

    if not caseSensitive:
        promptMessage = message + " ({})".format(lu.listToString(options,'/'))
    else:
        promptMessage = message + " (case sensitive) ({})".format(lu.listToString(options,'/'))

    np.infoPrint(promptMessage)

    #controllo non case sensitive
    if not caseSensitive:

        options = lu.toLowerAll(options)

        while True:
            choiche = str(input("> ")).lower()
            if choiche in options:
                return choiche
            
            else:
                print(errorMessage)


    #controllo case sensitive
    if caseSensitive:
        while True:
            choiche = str(input("> "))
            if choiche in options:
                return choiche
            
            else:
                print("Invalid choice. Please, retry.")