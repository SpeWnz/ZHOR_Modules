'''
Mini libreria per facilitare l'uso di termcolors
'''


from termcolor import colored, cprint
import platform


#fix per windows
if("Windows" in platform.system()):
    import colorama
    colorama.init()

# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    pass
else:
    pass


# ========================================================================================================================================================= 

def grey(message, end="\n"):
    cprint(message,'grey',end=end)

def red(message, end="\n"):
    cprint(message,'red',end=end)

def green(message, end="\n"):
    cprint(message,'green',end=end)

def yellow(message, end="\n"):
    cprint(message,'yellow',end=end)

def blue(message, end="\n"):
    cprint(message,'blue',end=end)

def magenta(message, end="\n"):
    cprint(message,'magenta',end=end)

def cyan(message, end="\n"):
    cprint(message,'cyan',end=end)

def white(message, end="\n"):
    cprint(message,'white',end=end)