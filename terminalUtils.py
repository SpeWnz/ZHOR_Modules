import os
import subprocess
import base64

# restituisce una lista contenente i terminali disponibili
def getAvailableTerminals(printResults=False):
    terminals = ['qterminal','xterm','gnome-terminal','terminator']

    availableTerminals = []
    for t in terminals:        
        
        try:
            out = str(subprocess.check_output(["which", t]))[2:-3]
            availableTerminals.append(t)

            if(printResults):
                print(t,"\r\t\t\t",out)

        except:
            if(printResults):
                print(t,"\r\t\t\t","N/A")

    return availableTerminals
        

#esegue un comando in una finestra di xterm
# -T title
# -e command
# esempio: xterm -T "provaprova123" -e "python2.7 -m SimpleHTTPServer 7707"
def spawn_xterm(command: str, windowTitle: str, workingDirectory=None,executeInBackground=True):
    
    if(workingDirectory is None):
        spawnStr = 'xterm -T "{}" -e "{}"'.format(windowTitle,command)
    else:
        spawnStr = 'xterm -T "{}" -e "cd {} && {}"'.format(windowTitle,workingDirectory,command)
    
    if(executeInBackground):
        spawnStr += " &"
    
    os.system(spawnStr)


def spawn_xterm_b64(command: str, windowTitle: str,executeInBackground=True,width=80,height=24,xPos=0,yPos=0):
    
    encodedBytes = base64.b64encode(command.encode('utf-8'))
    b64command = encodedBytes.decode('utf-8')

    spawnStr = 'xterm -T "{}" -geometry {}x{}+{}+{} -e "echo {} | base64 -d | sh"'.format(
        windowTitle,
        width,
        height,
        xPos,
        yPos,
        b64command
        )
    
    if(executeInBackground):
        spawnStr += " &"
    
    #subprocess.call(args=[spawnStr],shell=True)
    os.system(spawnStr)

#esegue un comando in una finestra di qterminal
def spawn_qterminal(command: str, workingDirectory=None,executeInBackground=True):
    
    if(workingDirectory is None):
        spawnStr = 'qterminal -e "{}"'
    else:
        spawnStr = 'qterminal --workdir "{}" -e "{}"'

    if(executeInBackground):
        spawnStr += " &"

    os.system(spawnStr)


#esegue un comando in una finestra di terminator
def spawn_terminator():
    raise NotImplementedError