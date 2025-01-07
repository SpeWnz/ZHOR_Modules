import requests

# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    import fileManager as fm
else:
    from . import fileManager as fm

# =============================================================================

BURP_PROXY_DEFAULT = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}


def requestFile2Headers(inputFile: str, startingIndex=0):
    lines = fm.fileToSimpleList(inputFile)

    d = {}
    for l in lines[startingIndex:]:
        values = l.split(": ")
        d[values[0]] = values[1]

    return d

def checkMalformedURL_HTTP(inputUrl: str):
    if "http://" not in inputUrl:
        inputUrl = "http://" + inputUrl

    return inputUrl


def checkMalformedURL_HTTPS(inputUrl: str):
    if "https://" not in inputUrl:
        inputUrl = "https://" + inputUrl

    return inputUrl


def isReachable_HTTP(inputUrl: str,verify=False,timeout=5):

    inputUrl = checkMalformedURL_HTTP(inputUrl)

    try:
        requests.get(url=inputUrl,verify=verify,timeout=timeout)
        return True
    except:
        return False

def isReachable_HTTPS(inputUrl: str,verify=False,timeout=5):
    inputUrl = checkMalformedURL_HTTPS(inputUrl)

    try:
        requests.get(url=inputUrl,verify=verify,timeout=timeout)
        return True
    except:
        return False


