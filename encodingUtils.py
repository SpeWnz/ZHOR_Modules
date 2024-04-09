import base64
import urllib.parse

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

