import pathlib
import ctypes
from subprocess import Popen, DETACHED_PROCESS, run

#Checks if database folder exists, if not, creates it
#and starts MongoDB
#Need to add password settings!
def startMongoDB():
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
def stopMongoDB():
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