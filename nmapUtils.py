# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    import nicePrints as np
    import fileManager as fm
    import listUtils as lu
else:
    from . import nicePrints as np
    from . import fileManager as fm
    from . import listUtils as lu
    
# =============================================================================

# legge un file di nmap e lo traduce in json
# [{},{},{}, .... {}]
def nmapTxtToJson(path: str):
    usefulLines = []
    fileLines = fm.fileToSimpleList(path)
    
    jsonObj = []

    #estrai solo righe necessarie
    for line in fileLines:
        if ("/tcp" in line):
            usefulLines.append(line)

    
    for item in usefulLines:
        
        #gestione splitting per spazio
        while "  " in item:
            item = item.replace("  "," ")

        #print(item)

        port = item.split('/')[0]
        service = item.split(' ')[2]
        version = lu.listToString(item.split(' ')[3:],' ')

        d = {"port":port,"service":service,"version":version}
        jsonObj.append(d)

    return jsonObj