# stuff for NO-FI-Zone
# https://github.com/SpeWnz/NO-FI-Zone

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


# OTHER MODULES
import sqlite3
import pandas as pd
import os

# =============================================================================

# wrapper for macchanger
# if the parameter "mac" is not specified, the mac is random.
# the mac must comply with the following format:
# XX:XX:XX:XX:XX:XX
def changeWlanCardMAC(wlanCard: str,mac=None):
    com1 = f'ifconfig {wlanCard} down'
    
    com2 = ""
    if mac is None:
        com2 = f'macchanger -r {wlanCard}'
    else:
        com2 = f'macchanger "{mac}" {wlanCard}'

    com3 = f'ifconfig {wlanCard} up'

    os.system(com1)
    os.system(com2)
    os.system(com3)


# Takes a airodump-ng csv file (not the one with "kismet" in its name)
# and produces a structured and organized sqlite db file.
# the overwrite parameter (if set to true) lets you delete the db and start all over
def airodump2sqlite(csvPath: str, outputDBpath: str,overWrite=False):
    '''
    Damn that's a huge function.
    What's up with all these currying and nested functions?

    This used to be a standalone script for "airodump-n-see", but i figured that
    i might re-use this for other scripts. So yeah... not really a pleasant view
    but it works.
    '''


    AP_CSV_HEADER = 'BSSID, First time seen, Last time seen, channel, Speed, Privacy, Cipher, Authentication, Power, # beacons, # IV, LAN IP, ID-length, ESSID, Key'
    STA_CSV_HEADER = 'Station MAC, First time seen, Last time seen, Power, # packets, BSSID, Probed ESSIDs'

    DATABASE        = None
    TEMP_AP_CSV     = '/tmp/__temp-ap.csv'
    TEMP_STA_CSV    = '/tmp/__temp-sta.csv'


    def get_sqlite_type(series):
        if pd.api.types.is_integer_dtype(series):
            return 'INTEGER'
        elif pd.api.types.is_float_dtype(series):
            return 'REAL'
        else:
            return 'TEXT'

    def mac2OUI(mac: str):
        return mac.strip()[0:8].replace(':','')

    # make the normalized and fixed stations csv file to feed into the db
    def makeSTAsCSV(csvLines: list):
        #np.debugPrint("Extracting and normalizing STAs data ...")
        fixedLines = ["Station_MAC, First_time_seen, Last_time_seen, Power, num_of_packets, BSSID, Probed_ESSIDs, ap_OUI, sta_OUI"]
        
        # gli ap stanno tra l'index <dove sta la scritta degli STA -1> e la "fine -1 "
        STA_linesIndex = 0
        for line in csvLines:
            if STA_CSV_HEADER in line:
                break # trovato
            else:
                STA_linesIndex += 1

        # qui Ã¨ gia senza csv header
        STA_lines = csvLines[STA_linesIndex + 1:-1]

        for l in STA_lines:
            
            # probe requests are from index 6 on
            values = l.split(',')
            probes = values[6:]

            staMac = values[0]
            apMac = values[5]

            staOUI = mac2OUI(staMac)

            # is it a case where we have a "not associated" client?
            if ':' in apMac:
                apOUI = mac2OUI(apMac)
            else:
                apOUI = ""

            #print(probes)

            for p in probes:
                fixedLine = lu.concatenate_elements(values[0:6],',') + f',"{p}",{apOUI},{staOUI}'
                #print(fixedLine)
                fixedLines.append(fixedLine)

        fm.listToFile(fixedLines,TEMP_STA_CSV)

    # make the fixed csv file to feed into the db  
    def makeAPsCSV(csvLines: list):
        #np.debugPrint("Extracting APs data ...")

        # gli ap stanno tra l'index 2 e <dove sta la scritta degli STA -2>
        AP_linesIndex = 0
        for line in csvLines:
            if STA_CSV_HEADER in line:
                break
            else:
                AP_linesIndex += 1

        AP_lines = csvLines[2:AP_linesIndex - 1]

        fixedLines = ["BSSID, First_time_seen, Last_time_seen, channel, Speed, Privacy, Cipher, Authentication, Power, num_beacons, num_IV, LAN_IP, ID_length, ESSID, Key, ap_OUI"]
        for l in AP_lines:
            
            values = l.split(',')
            staMac = values[0]
            staOUI = mac2OUI(staMac)

            fixedLine = f'{l},{staOUI}'
            fixedLines.append(fixedLine)

        fm.listToFile(fixedLines,TEMP_AP_CSV) 


    # creates the database to store airodump information
    def createDatabase(database: str):
        #np.debugPrint(f"Database {database} does not exist. Creating it.")
        db = sqlite3.connect(database)
        cursor = db.cursor() 

        # create ap table
        #np.debugPrint("Creating ap table ...")
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS access_points (BSSID TEXT,  First_time_seen TEXT,  Last_time_seen TEXT,  channel INTEGER,  Speed INTEGER,  Privacy TEXT,  Cipher TEXT,  Authentication TEXT,  Power INTEGER,  num_beacons INTEGER,  num_IV INTEGER,  LAN_IP TEXT,  ID_length INTEGER,  ESSID TEXT,  Key TEXT,  ap_OUI TEXT)''')

        # create sta table
        #np.debugPrint("Creating sta table ...")
        cursor.execute('''CREATE TABLE IF NOT EXISTS stations (Station_MAC TEXT,  First_time_seen TEXT,  Last_time_seen TEXT,  Power INTEGER,  num_of_packets INTEGER,  BSSID TEXT,  Probed_ESSIDs TEXT,  ap_OUI TEXT,  sta_OUI TEXT)''')

        # create scope table
        cursor.execute('''CREATE TABLE IF NOT EXISTS "scope_networks" (
        "ESSID"	TEXT,
        "Privavcy"	TEXT,
        "Authentication" TEXT
        );''')

        db.commit()
        db.close()

    # used to feed either the APs or the STAs table
    def feedData(inputCsv: str, dbTable: str):
        
        
        #np.debugPrint(f"Feeding {inputCsv} into table {dbTable} ...")
        df = pd.read_csv(inputCsv)
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

        # Create SQLite database and connect to it
        db_file_path = DATABASE  # SQLite database file
        conn = sqlite3.connect(db_file_path)
        cursor = conn.cursor()

        # Create the table based on CSV columns and types
        columns = df.columns.tolist()
        column_defs = []

        # insert access points information
        for col in columns:
            column_type = get_sqlite_type(df[col])
            column_defs.append(f"{col} {column_type}")


        # Insert data into the table
        for row in df.itertuples(index=False, name=None):
            com = "INSERT INTO {} ({}) VALUES ({})".format(
                dbTable,
                ', '.join(columns),
                ', '.join(['?'] * len(row))
            )
            cursor.execute(com, row)

        # Commit and close
        conn.commit()
        conn.close()

    # remove temporary files
    def cleanup():
        #np.debugPrint("Cleaning up temporary files...")
        os.remove(TEMP_AP_CSV)
        os.remove(TEMP_STA_CSV)


    # ------------------- pseudo main
    DATABASE = outputDBpath

    if(overWrite):
        os.remove(DATABASE)

    # create the database if it doesn't exist
    if not os.path.isfile(DATABASE):
        createDatabase(DATABASE)

    csvLines = fm.fileToSimpleList(csvPath)
        
    makeAPsCSV(csvLines)
    makeSTAsCSV(csvLines)

    feedData(TEMP_AP_CSV,'access_points')
    feedData(TEMP_STA_CSV,'stations')

    cleanup()