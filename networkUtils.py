# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    import nicePrints as np
    import random
else:
    from . import nicePrints as np
    import random

# =============================================================================



# genera un indirizzo mac casuale
# può prendere in input una lista di indirizzi mac che devono essere diversi dal risultato
def randomMACAddress(differentFrom: list = None):
    
    # prima creazione
    mac = mac = str("%02x:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
        ))
    
    # verifica di eventuali mac già esistenti
    if differentFrom is None:
        return mac

    else:

        print("verifico se",mac,"si trova in ",differentFrom)
        while mac in differentFrom:
            mac = str("%02x:%02x:%02x:%02x:%02x:%02x" % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
            ))

        return mac


#print(randomMACAddress(["9a:54:47:8a:3f:a0","b9:50:9e:21:9a:87"]))