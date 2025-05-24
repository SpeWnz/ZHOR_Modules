import base64
import urllib.parse
import re

# input: string and regex
# output: string without characters that do not match the regex
def stringRegexSanify(inputString: str, regex):
    return ''.join(re.findall(regex,inputString))

def urlEncode_encodeString(input_string):
    # Encode the input string with URL encoding
    encoded_string = urllib.parse.quote_plus(input_string)
    return encoded_string

def base64_encodeString(input_string: str):
    # Encode the input string to bytes using utf-8 encoding
    input_bytes = input_string.encode('utf-8')
    
    # Use base64 encoding to encode the bytes
    encoded_bytes = base64.b64encode(input_bytes)
    
    # Decode the bytes back to string and return
    encoded_string = encoded_bytes.decode('utf-8')
    
    return encoded_string

# # bash -c {echo,bHMgLWFsCg==}|{base64,-d}|{bash,-i}
def bashEncode_command(inputCommand: str):
    base64Command = base64_encodeString(inputCommand)
    bashCommand = "bash -c {echo," + base64Command + "}|{base64,-d}|{bash,-i}"
    return bashCommand

# screw you urllib for makin' me do this manually
def urlEncode_allSpecialCharacters(inputString: str):
    d = {
        " ": "%20",
        "-": "%2D",
        "{": "%7B",
        "}": "%7D",
        ",": "%2C",
        "=": "%3D",
        "|": "%7C"
    }

    d2 = {
        " ": "%20",
        "!": "%21",
        "\"": "%22",
        "#": "%23",
        "$": "%24",
        "%": "%25",
        "&": "%26",
        "'": "%27",
        "(": "%28",
        ")": "%29",
        "*": "%2A",
        "+": "%2B",
        ",": "%2C",
        "-": "%2D",
        ".": "%2E",
        "/": "%2F",
        ":": "%3A",
        ";": "%3B",
        "<": "%3C",
        "=": "%3D",
        ">": "%3E",
        "?": "%3F",
        "@": "%40",
        "[": "%5B",
        "\\": "%5C",
        "]": "%5D",
        "^": "%5E",
        "_": "%5F",
        "`": "%60",
        "{": "%7B",
        "|": "%7C",
        "}": "%7D",
        "~": "%7E",
        "€": "%E2%82%AC",
        "£": "%C2%A3",
        "¥": "%C2%A5",
        "©": "%C2%A9",
        "®": "%C2%AE",
        "™": "%E2%84%A2",
        "÷": "%C3%B7",
        "×": "%C3%97",
        "μ": "%CE%BC",
        "α": "%CE%B1",
        "β": "%CE%B2",
        "γ": "%CE%B3",
        "δ": "%CE%B4",
        "ε": "%CE%B5",
        "θ": "%CE%B8",
        "λ": "%CE%BB",
        "π": "%CF%80",
        "σ": "%CF%83",
        "τ": "%CF%84",
        "ω": "%CF%89"
    }
    
    outputString = ""
    for char in inputString:
        if char in d2:
            outputString += d2[char]
        else:
            outputString += char
    return outputString