import pathlib
import os
import re
import ctypes
from subprocess import Popen
from shutil import which

def selectFile(file,program=False):
  if program == False:
    program = file
  path = pathlib.Path(__file__).parent.iterdir()
  dirs = list(filter(lambda path: path.is_dir(), path))
  dir = [x for x in dirs if program in x.name][0].iterdir()
  binDir = list(filter(lambda path: path.is_dir(), dir))[0].iterdir()
  bin = [x for x in binDir if file+'.exe' in x.name.lower()][0]
  return bin

#checks
def checkPATH(path, env):
  p = str(path)[0].upper() + str(path)[1:]
  if p in env:
    return True
  else:
    return False

def setPath(path, env, ignoreRegex=False):
  p = str(path)[0].upper() + str(path)[1:]

  #Replace absolute paths prefixes with wildcards
  if ignoreRegex == False:
    env = [sub.replace('C:\WINDOWS', '%SystemRoot%') for sub in env]
    env = [(re.sub(r'(.*)\\Users\\(.*)\\AppData',"%USERPROFILE%\\\\AppData",x)) for x in env]
  
  #if Path is not in environment Variables, add it
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

#Runs powershell install script for Compass
def installCompass():
  file = selectFile('compass','mongodb')[0]
  Popen([
    "powershell.exe",
    str(file)
  ])

#checks if Compass and MongoDB are in path, if not install them
def setupMongoDB():
  env = str(os.getenv('PATH')).split(';')
  env = [x for x in env if x != '']
  files = ('mongod','mongosh')
  user = os.getlogin()
  cpath = 'C:\\Users\\'+user+'\\AppData\\Local\\MongoDBCompass'
  for file in files:
    f = selectFile(file)
    folder = f.parent
    if checkPATH(folder, env) == False:
      env = setPath(folder, env)
  
  if which('MongoDBCompass') is None:
    installCompass()
    setPath(cpath, env)

setupMongoDB()