# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    import fileManager as fm
    import nicePrints as fm
else:
    from . import nicePrints as np
    from . import fileManager as fm

# OTHER MODULES
from bs4 import BeautifulSoup
import csv

# =============================================================================


np.errorPrint("csvTools.py is deprecated. Use csvUtils.py instead.")


# riversa i dati (le righe) di un file strutturato tipo csv in una lista di liste
# dove ogni sottolista contiene tutti i valori di una certa riga che sono separati da ';'
# Esempio: 
#           val1;val2;val3
#           val4;val5;val6
# Diventa
#           [[val1,val2,val3],[val4,val5,val6]]
def fileToCSVList(inputFile):
    fileLines = open(inputFile, 'r').readlines()
    outputList = []

    for lines in fileLines:
        lines = lines.rstrip("\n").split(';')
        outputList.append(lines)

    return outputList

# verifica se un file csv ha tutte le righe hanno lo stesso numero di valori o no
def allRowsHaveSameLength(inputFile):
    csvList = fileToCSVList(inputFile)
    it = iter(csvList)
    the_len = len(next(it))

    if not all(len(l) == the_len for l in it):
        return False
    else:
        return True


# Converte un file csv in una tabella html.
# styleFile consente di specificare un percorso in cui si trova un file .css per specificare lo stile della tabella
# ATTENZIONE: il foglio di stile può contenere solo personalizzazioni riguardanti le seguenti tag:
# th, td, td
# Dare un'occhiata al file DEFAULT_TABLE_STYLE.css per capire di che si tratta
def makeHTMLTable(inputFile,outputFile,columns,styleFile=None):

    #controlla se columns è una lista o no
    if type(columns) is not list:
        raise Exception("ERRORE: la variabile \"columns\" non è di tipo list. Deve essere usata una lista con i nomi delle colonne.")
        

    MIO_FILE = inputFile            #nome del csv in input
    OUTPUT_FILE_PATH = outputFile   #nome del html in output
    COLUMN_NAMES = columns          #nomi delle colonne
    HTML_LINES = []                 #righe del file html da scrivere


    csv_file = open(MIO_FILE, 'r').readlines()

    HTML_LINES.append("<html>")
    HTML_LINES.append("<body>")
    HTML_LINES.append("<table>")

    #definizione dello stile della tabella
    HTML_LINES.append("<style>")

    if (styleFile is None):
        styleList = fileManager.fileToSimpleList("DEFAULT_TABLE_STYLE.css")
    else:
        styleList = fileManager.fileToSimpleList(styleFile)

    HTML_LINES += styleList
    HTML_LINES.append("</style>")

    #titolo delle colonne della tabella
    HTML_LINES.append("<tr>")
    for name in COLUMN_NAMES:
        HTML_LINES.append("<th> " + name + "</th>")

    HTML_LINES.append("</tr>")

    #altre righe della tabella
    for line in csv_file:
        HTML_LINES.append("<tr>")

        line = line.rstrip("\n")
        elements = line.split(';')

        for element in elements:
            HTML_LINES.append("<td>" + element + "</td>")
            #input()

        HTML_LINES.append("</tr>")

    HTML_LINES.append("</table>") 
    HTML_LINES.append("</body>")
    HTML_LINES.append("</html>")


    # scrivo il tutto su un file html
    with open(OUTPUT_FILE_PATH,'w') as f:
        for html_line in HTML_LINES:
            f.write("%s\n" % html_line)


# Converte un file html contentente LA SOLA TAG PER LA TABELLA
# (si suppone quindi di avere a che fare con un file creato apposta per contenere solo quella tabella)
def htmlTableToCSV(inputFile: str, outputFileName: str):
    file = open(inputFile,'r')
    soup = BeautifulSoup(file,features='lxml')
    table = soup.find('table')
    headers = [str(th.text) for th in table.select("tr th")]

    with open(outputFileName, "w") as f:
        wr = csv.writer(f)
        wr.writerow(headers)
        wr.writerows([[td.text.encode("utf-8") for td in row.find_all("td")] for row in table.select("tr + tr")])
