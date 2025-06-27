import subprocess
import os
import platform

# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    pass
else:
    pass


# ========================================================================================================================================================= 

def isWindows():
    if("Windows" in platform.system()):
        return True
    else:
        return False

def clear():
    if isWindows():
        os.system("cls")
    else:
        os.system("clear")

def deleteFile(fileName: str):
    if isWindows():
        os.system("del " + fileName)
    else:
        os.system("rm " + fileName)


def pressEnterToExit(newLines=0):
    for i in range(0,newLines):
        print("\n",end='')

    input("Press enter to exit the application")
    exit()

def pressEnterToContinue(msg="Press enter to continue"):
    input(msg)


# returns stdout and stderr of a command
# usage: stdout, stderr = commandResult(" ... ")
def commandResult(command):
    #print("COMMAND RESULT")
    
    if type(command) is str:
        result = subprocess.run(command.split(' '),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')
    
    if type(command) is list:
        result = subprocess.run(command,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')




def countLines(filePath: str):
    com = ['wc','-l',filePath]
    count, _ = commandResult(com)
    count = count.split(' ')[0]
    
    
    return int(count) + 1
    
def splitFile_parts(filePath: str, parts: int,suffix: str):
    com = 'split -n {} "{}" --additional-suffix "{}"'.format(str(parts),filePath,suffix)
    os.system(com)

def splitFile_lines(filePath: str, lines: int,suffix: str):
    com = 'split -l {} "{}" --additional-suffix "{}"'.format(str(lines),filePath,suffix)
    os.system(com)


# takes an absolute path and returns a list of all files within it (with the absolute path prepended to them)
# if specified, it can also return the list of files without the prepended absolute path (as a second return), via the "returnFiles" parameter
def dirPathLS(absolutePath: str, returnFiles=False):
    files = os.listdir(absolutePath)
    outputList = []

    for f in files:
        if isWindows():
            outputList.append(absolutePath + "\\" + f)
        else:
            outputList.append(absolutePath + "/" + f)

    if not returnFiles:
        return outputList
    
    else:
        return outputList, files
