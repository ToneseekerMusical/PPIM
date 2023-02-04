import pathlib
import os
import re
import ctypes
from subprocess import Popen
from shutil import which

def selectPATH(file,program=False):
  if program == False:
    program = file
  path = pathlib.Path(__file__).parent.iterdir()
  dirs = list(filter(lambda path: path.is_dir(), path))
  if file in ('mongodb', 'mongosh'):
    binDir = [x for x in dirs if program in x.name][0].iterdir()
    bin = list(filter(lambda path: path.is_dir(), binDir))[0]
    return bin
  else:
    dir = [x for x in dirs if program in x.name.lower()][0]
    return dir

#checks
def checkPATH(paths:list, env):
  pathlist = []
  for path in paths:
    p = str(path)[0].upper() + str(path)[1:]
    if p not in env:
      pathlist.append(p)
  return(pathlist)

def setPath(paths:list, env, ignoreRegex=False):
  #Replace absolute paths prefixes with wildcards
  if ignoreRegex == False:
    env = [sub.replace('C:\WINDOWS', '%SystemRoot%') for sub in env]
    env = [(re.sub(r'(.*)\\Users\\(.*)\\AppData',"%USERPROFILE%\\\\AppData",x)) for x in env]
    for path in paths:
      env.append(path)
    env = sorted([*set(env)])
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

#checks if Compass and MongoDB are in path, if not install them
def setupPATH():
  env = str(os.getenv('PATH')).split(';')
  env = [x for x in env if x != '']
  files = ('mongodb','mongosh','compass','node','vscode')
  paths = []
  for file in files:
    paths.append(selectPATH(file))
  paths = checkPATH(paths,env)
  if len(paths) > 0:
    print(str(len(paths))+' file(s) not in path')
    env = setPath(paths, env)

setupPATH()