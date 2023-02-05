import pathlib
import ctypes
from subprocess import Popen

#Checks if database folder exists, if not, creates it
#and starts MongoDB
#Need to add password settings!
def firstDBStart():
    path = pathlib.Path()
    cwd = str(path.cwd())
    srv = path.joinpath(cwd+'\\srv\\mongodb')
    if srv.is_dir() == False:
       srv.mkdir(parents=True)
    print(srv.is_dir())
    Popen([
      "mongod.exe",
      "--dbpath", str(srv)+'\\',
    ])

firstDBStart()

def startDB():
    path = pathlib.Path()
    cwd = str(path.cwd())
    srv = path.joinpath(cwd+'\\srv\\mongodb\\')
    srvPath = path.joinpath(str(path)+'/srv/mongodb')
    if srvPath.is_dir() == False:
      srvPath.mkdir(parents=True)

    Popen([
      "mongod.exe",
      "--dbpath", str(srvPath),
    ])

#Cannot Shut Down MongoDB at this time
def stopDB():
    commands = u"pkill -2 $USER mongodb"
    
    ctypes.windll.shell32.ShellExecuteW(
      None,
      u"runas",
      u"powershell.exe",
      commands,
      None,
      1
    )

#Starts Compass
def startCompass():
   Popen('mongodbcompass.exe')