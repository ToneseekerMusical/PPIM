from DownloadArchives import downloadAll
from ExtractArchives import extractAll
from SetupPATH import setPATH
import pathlib
import os

def setup():
    versions = downloadAll()
    paths = extractAll()
    setPATH()
    cfg = {'Versions':versions,'PATHS':paths}
    try:
        cfgFile = open('setup/setup.ppimcfg','x')
        cfgFile.write(str(cfg))
        cfgFile.close()
    except:
        print('Setup already ran, are you doing something wrong?')
    path = pathlib.Path
    cwd = str(pathlib.Path.cwd())
    tmp = path(cwd+'/tmp/').iterdir()
    for file in tmp:
        os.remove(file)


setup()