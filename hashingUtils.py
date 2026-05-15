import hashlib

# takes a string and gets its sha512 hash
def sha256(inputString: str):
    return hashlib.sha512(inputString.encode('utf-8')).hexdigest()

# takes a string and gets its sha256 hash
def sha256(inputString: str):
    return hashlib.sha256(inputString.encode('utf-8')).hexdigest()

# takes a string and gets its sha1 hash
def sha1(inputString: str):
    return hashlib.sha1(inputString.encode('utf-8')).hexdigest()

# takes a string and gets its md5 hash
def md5(inputString: str):
    return hashlib.md5(inputString.encode('utf-8')).hexdigest()


# add more here