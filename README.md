# ZHOR_Modules -  Modules and utilities for Python3


## Global Install

### Linux
<p>On Linux, clone this repo inside the Python3 "dist-packages" folder, then install the requirements like so:<p>

```
sudo git clone https://github.com/SpeWnz/ZHOR_Modules /usr/lib/python3/dist-packages/ZHOR_Modules
pip install -r /usr/lib/python3/dist-packages/ZHOR_Modules/requirements.txt --break-system-packages
```
</code> </p>

### Windows
<p>On Windows, "git clone" this repo inside the Python3 "site-packages" folder. Usually it would be:</p>

```
git clone https://github.com/SpeWnz/ZHOR_Modules C:\Users\USERNAME\AppData\Roaming\Python\Python310\site-packages\ZHOR_Modules
pip install -r C:\Users\USERNAME\AppData\Roaming\Python\Python310\site-packages\ZHOR_Modules\requirements.txt
```

<p>Of course, replace "Python310" with the version you own.</p>

## Virtual Environment

You may need or prefer to install the required stuff into a venv (virtual environment). To do so, follow the steps below:

1. Set up the venv:
```
(generic linux shell)
python3 -m venv .venv; source .venv/bin/activate

(fish shell)
python3 -m venv .venv; source .venv/bin/activate.fish

(windows powershell)
python -m venv .venv; .\.venv\Scripts\activate.ps1
```

2. Place ZHOR_Modules in the respective venv folder.

For linux, follow these steps (replace python3.13 with the version you own)
```
mkdir .venv/lib/python3.13/dist-packages
git clone https://github.com/SpeWnz/ZHOR_Modules .venv/lib/python3.13/dist-packages/ZHOR_Modules
cat .venv/lib/python3.13/dist-packages/ZHOR_Modules/requirements.txt | xargs -I {} pip install {}
```

For Windows, follow these steps:

```
cd .venv/Lib/site-packages/
git clone https://github.com/SpeWnz/ZHOR_Modules
pip install -r requirements.txt
```
