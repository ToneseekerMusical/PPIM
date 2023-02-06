from Install.DownloadArchives import downloadAll
from Install.ExtractArchives import extractAll
from Install.SetupPATH import setPATH
import pathlib
import os

def setup():
    versions = downloadAll()
    paths = extractAll()
    setPATH()
    cfg = {"versions":versions,"PATHS":paths}
    try:
        cfgFile = open('Install/setup.ppimcfg','w')
        cfgFile.write(str(cfg))
        cfgFile.close()
    except:
        print('Setup already ran, are you doing something wrong?')
    path = pathlib.Path
    cwd = str(pathlib.Path.cwd())
    tmp = path(cwd+'/tmp/').iterdir()
    for file in tmp:
        os.remove(file)