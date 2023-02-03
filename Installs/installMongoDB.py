import pathlib
import os
import re
import ctypes
from subprocess import Popen, CREATE_NEW_CONSOLE

def selectFile(file):
    path = pathlib.Path(__file__).parent.iterdir()
    dirs = list(filter(lambda path: path.is_dir(), path))
    mongoDir = [x for x in dirs if 'mongo' in x.name][0].iterdir()
    mongoBin = list(filter(lambda path: path.is_dir(), mongoDir))[0].iterdir()
    bin = [x for x in mongoBin if file in x.name.lower()]
    return bin

def setPATH(path):
  p = str(path)[0].upper() + str(path)[1:]
  env=os.getenv('PATH')
  env=env.split(';')
  env = [x for x in env if x != '']
  env = [sub.replace('WINDOWS', '%SystemRoot%') for sub in env]
  env = [(re.sub(r'(.*)\\Users\\(.*)\\AppData',"%USERPROFILE%\\\\AppData",x)) for x in env]

  if p not in env:
    print(p)
    env.append(p)
    env = ';'.join(env)
    var = "PATH"
    scope = "Machine"
    commands = u"[Environment]::SetEnvironmentVariable('"+var+"','"+env+"','"+scope+"')"
    ctypes.windll.shell32.ShellExecuteW(
      None,
      u"runas",
      u"powershell.exe",
      commands,
      None,
      1
    )
        

def startMongos():
    file = 'mongos.exe'
    file = selectFile(file)[0]
    folder = file.parent
    setPATH(folder)
    Popen([
      "mongos.exe",
    ], creationflags=CREATE_NEW_CONSOLE)

def startMongod():
    path = pathlib.Path()
    if path.is_dir():
       path.joinpath('/srv/mongodb')
    else:
       path.mkdir(parents=True)

    print(path)
       
    file = 'mongod.exe'
    file = selectFile(file)[0]
    folder = file.parent
    setPATH(folder)
    Popen([
      "mongod.exe",
      "--dbpath", str(path),
      "--port", "27019"
    ], creationflags=CREATE_NEW_CONSOLE)

startMongod()
startMongos()