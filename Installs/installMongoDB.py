import pathlib
import os
import re
import ctypes
from subprocess import Popen
from shutil import which

def selectFile(file):
  path = pathlib.Path(__file__).parent.iterdir()
  dirs = list(filter(lambda path: path.is_dir(), path))
  mongoDir = [x for x in dirs if 'mongo' in x.name][0].iterdir()
  mongoBin = list(filter(lambda path: path.is_dir(), mongoDir))[0].iterdir()
  bin = [x for x in mongoBin if file in x.name.lower()]
  return bin

def checkPATH(path, env):
  p = str(path)[0].upper() + str(path)[1:]
  if p in env:
    return True
  else:
    return False

def setPath(path, env):
  p = str(path)[0].upper() + str(path)[1:]

  #remove empty values
  env = [x for x in env if x != '']

  #Replace absolute paths prefixes with wildcards
  env = [sub.replace('C:\WINDOWS', '%SystemRoot%') for sub in env]
  env = [(re.sub(r'(.*)\\Users\\(.*)\\AppData',"%USERPROFILE%\\\\AppData",x)) for x in env]
  
  if p not in env:
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
  print('Set Path Ran!')
  return env

def installCompass():
  file = 'compass'
  file = selectFile(file)[0]
  Popen([
    "powershell.exe",
    str(file)
  ])
        
def setupMongoDB():
  file = 'mongo'
  file = selectFile(file)[0]
  folder = file.parent
  cpath = '%USERPROFILE%\AppData\Local\MongoDBCompass'
  env = str(os.getenv('PATH')).split(';')
  compass = which('MongoDBCompass')
  
  if checkPATH(folder, env) == False:
    env = setPath(folder, env)
  
  if compass is None:
    installCompass()
    setPath(cpath, env)

setupMongoDB()