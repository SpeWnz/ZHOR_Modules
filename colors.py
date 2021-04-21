'''
Mini libreria per facilitare l\'uso di termcolors
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

def grey(coloredMessage,nonColoredMessage="", END="\n"):
    cprint(coloredMessage,'grey',end='')
    print(nonColoredMessage,end=END)

def red(coloredMessage,nonColoredMessage="", END="\n"):
    cprint(coloredMessage,'red',end='')
    print(nonColoredMessage,end=END)

def green(coloredMessage,nonColoredMessage="", END="\n"):
    cprint(coloredMessage,'green',end='')
    print(nonColoredMessage,end=END)

def yellow(coloredMessage,nonColoredMessage="", END="\n"):
    cprint(coloredMessage,'yellow',end='')
    print(nonColoredMessage,end=END)

def blue(coloredMessage,nonColoredMessage="", END="\n"):
    cprint(coloredMessage,'blue',end='')
    print(nonColoredMessage,end=END)

def magenta(coloredMessage,nonColoredMessage="", END="\n"):
    cprint(coloredMessage,'magenta',end='')
    print(nonColoredMessage,end=END)

def cyan(coloredMessage,nonColoredMessage="", END="\n"):
    cprint(coloredMessage,'cyan',end='')
    print(nonColoredMessage,end=END)

def white(coloredMessage,nonColoredMessage="", END="\n"):
    cprint(coloredMessage,'white',end='')
    print(nonColoredMessage,end=END)