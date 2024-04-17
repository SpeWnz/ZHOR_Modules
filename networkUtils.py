# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    import nicePrints as np  
else:
    from . import nicePrints as np
    

import random
import re
import ipaddress
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



# data una stringa estrae l'ip usando espressioni regolari (regex)
def parseIP_fromString(inputString: str):
    return re.findall( r'[0-9]+(?:\.[0-9]+){3}', inputString)





def get_ip_range(start_ip, end_ip):
    # Convert the start and end IP addresses to IPv4Address objects
    start = ipaddress.IPv4Address(start_ip)
    end = ipaddress.IPv4Address(end_ip)
    
    # Iterate over the IP address range and print each IP address
    current_ip = start
    out = []
    while current_ip <= end:
        print(str(current_ip))
        current_ip += 1
        out.append(current_ip)

    return out