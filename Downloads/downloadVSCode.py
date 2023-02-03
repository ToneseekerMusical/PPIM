# imported the requests library
from urllib.request import urlretrieve

def downloadVSCode():
    vscode_url = "https://update.code.visualstudio.com/latest/win32-x64-archive/stable"

    urlretrieve(vscode_url,'VSCode.zip')

downloadVSCode()