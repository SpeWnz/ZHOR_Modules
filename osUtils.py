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