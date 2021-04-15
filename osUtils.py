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

