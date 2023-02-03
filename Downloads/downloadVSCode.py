# imported the requests library
from urllib.request import urlopen, urlretrieve
import os

def downloadVSCode():
    vscode_url = "https://update.code.visualstudio.com/latest/win32-x64-archive/stable"
    vscodeVer = urlopen(vscode_url)
    contentdisposition = vscodeVer.info()['Content-Disposition']
    filename = contentdisposition.split('"')[1]
    if not os.path.exists('Installs/'+filename):
        urlretrieve(vscode_url, 'Installs/'+filename)
    else:
        print('LTS VS Code already downloaded')