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
def commandResult(command: str):
    #print("COMMAND RESULT")
    result = subprocess.run(command.split(' '),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')


def countLines(filePath: str):
    com = "wc -l {}".format(filePath)
    count, _ = commandResult(com)
    count = count.split(' ')[0]
    
    return int(count) + 1
    
def splitFile_parts(filePath: str, parts: int,suffix: str):
    com = 'split -n {} "{}" --additional-suffix "{}"'.format(str(parts),filePath,suffix)
    os.system(com)

def splitFile_lines(filePath: str, lines: int,suffix: str):
    com = 'split -l {} "{}" --additional-suffix "{}"'.format(str(lines),filePath,suffix)
    os.system(com)
