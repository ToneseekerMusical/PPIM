import pathlib
from subprocess import Popen, DETACHED_PROCESS, run
from shutil import which

#Checks if database folder exists, if not, creates it
#and starts MongoDB
#Need to add password settings!
def startMongoDB():
    path = pathlib.Path(__file__).parent.parent
    srvPath = path.joinpath(str(path)+'/srv/mongodb')
    if srvPath.is_dir() == False:
      srvPath.mkdir(parents=True)

    Popen([
      "mongod.exe",
      "--dbpath", str(srvPath),
    ], creationflags=DETACHED_PROCESS)

#Cannot Shut Down MongoDB at this time
def stopMongoDB():
   Popen([
      "mongod.exe",
      "--shutdown"
   ])

#Starts Compass
def startCompass():
   Popen('mongodbcompass.exe')

startCompass()