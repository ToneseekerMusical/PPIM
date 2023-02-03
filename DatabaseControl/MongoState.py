import pathlib
from subprocess import Popen, DETACHED_PROCESS, run
from shutil import which

#Which is returning none even though programs are in system path

def selectFile(path,file):
  path = path.iterdir()
  path = list(filter(lambda path: path.is_dir(), path))
  path = [x for x in path if 'mongo' in x.name][0].iterdir()
  path = list(filter(lambda path: path.is_dir(), path))[0].iterdir()
  bin = [x for x in path if file in x.name.lower()]
  return bin

def startMongoDB():
    path = pathlib.Path(__file__).parent.parent
    srvPath = path.joinpath(str(path)+'/srv/mongodb')
    if srvPath.is_dir() == False:
      srvPath.mkdir(parents=True)
    print(srvPath)

    Popen([
      "mongod.exe",
      "--dbpath", str(srvPath),
    ], creationflags=DETACHED_PROCESS)

def stopMongoDB():
   Popen([
      "mongod.exe",
      "--shutdown"
   ])

def startCompass():
   run('MongoDBCompass')

print(which('MongoDBCompass'))