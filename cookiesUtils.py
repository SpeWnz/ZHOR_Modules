# example: _ga=xxxxxxxxxxx; _gid=xxxxxxxxxxxxxx; _gat=1
def cookieStringToDict(cookieString: str):
    outputDict = {}
    cookieString = cookieString.replace(" ",'')

    values = cookieString.split(";")

    for item in values:
        c = item.split('=')
        outputDict[c[0]] = c[1]

    return outputDict

# converte una stringa cookie in un formato di cookie accettabile da selenium webdriver.
# restituisce una lista di singoli cookie, dove ogni cookie è del seguente formato
# {'name' : COOKIE_KEY, 'value' : COOKIE_VALUE, 'domain' : EXAMPLE.COM}
# Poichè restituisce una lista, sarà necessario poi fare la seguente operazione per ogni oggetto della lista
# > browser.add_cookie(cookie)
# L'url richiesto è l'url su cui naviga il webdriver e sul quale vanno usati i cookie
def cookieStringToSelenium(cookieString: str,url: str):
    cookieDict = cookieStringToDict(cookieString)

    domain = ""
    if ("https://" in url):
        domain = url.split("https://")[-1]

    if ("http://" in url):
        domain = url.split("http://")[-1]

    cookieDictList = []
    for item in cookieDict:
        d = {'name' : item, 'value' : cookieDict[item], 'domain' : domain}

        cookieDictList.append(d)

    return cookieDictList




