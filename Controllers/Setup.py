import ctypes, json, os, re
from pathlib import Path as Path

import pymongo.database as Database

import Controllers.Mongo as Mongo
import Controllers.System as System
from Controllers.Download import downloadAll, extractAll


class Setup():
  def __init__(self):...


def setup():
    cwd = str(Path.cwd())
    Paths = extractAll()
    versions = downloadAll()
    tmp = Path(cwd+'/tmp/').iterdir()
    setPath()
    cfg = {"versions":versions,"PathS":Paths}
    try:
        cfgFile = open('Install/setup.ppimcfg','w')
        cfgFile.write(str(cfg).replace("'",'"'))
        cfgFile.close()
    except:
        print('Setup already ran, are you doing something wrong?')
    for file in tmp:
        os.remove(file)

def PPIMdbSetup():
  cwd = str(Path.cwd())
  srv = Path(cwd+'\\srv\\mongodb')
  conft = Path(cwd+'\\Install\\mongod.conf')
  conf = Path(cwd+'\\lib\\mongodb\\bin\\mongod.conf')
  
  if srv.is_dir() == False: srv.mkdir(parents=True)
  
  confc = open(conft,'r').read()
  confc = confc.replace('<logPath>',str(srv)+'\\mongo.log')
  confc = confc.replace('<PIDPath>',str(srv)+'\\mongo.pid')
  confc = confc.replace('<TzDBPath>',str(srv))
  confc = confc.replace('<storagePath>',str(srv))
  conff = open(conf,'w')
  conff.write(confc)
  conff.close()
  
  Path(str(srv)+'\\mongod.pid').touch()
  Path(str(srv)+'\\mongod.log').touch()
  if not System.get_service('MongoDB'):
    ctypes.windll.shell32.ShellExecuteW(
      None,
      "runas",
      "powershell.exe",
      """
      mongod --config {conf} --install --serviceName MongoDB;
      net start MongoDB
      """.format(conf=str(conf)),
      None,
      0
    )

  sysinf = json.load(open(Path(cwd+'\\Install\\setup.ppimcfg')))
  db = Mongo.dbConnect(
    "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=PPIM",
    "PPIM"
    )
  try:
    system = Database.Database.create_collection(db,'System',check_exists=True,capped=True,max=1,size=52428800)
    settings = Database.Database.create_collection(db,'Settings',check_exists=True,capped=True,max=1,size=52428800)
  except:
    system = Database.Database.get_collection(db,'System')
  try:
    system.insert_one(sysinf)
  except:
    pass

def selectPath(file,program=False):
  if program == False:
    program = file
  cwd = str(Path.cwd())
  deps = Path(cwd+'\\lib\\').iterdir()
  dirs = list(filter(lambda Path: Path.is_dir(), Path))
  if file in ('mongodb', 'mongosh'):
    binDir = [x for x in dirs if program in x.name][0].iterdir()
    bin = list(filter(lambda Path: Path.is_dir(), binDir))[0]
    return bin
  else:
    dir = [x for x in dirs if program in x.name.lower()][0]
    return dir

#checks
def checkPath(Paths:list, env):
  Pathlist = []
  for Path in Paths:
    p = str(Path)[0].upper() + str(Path)[1:]
    if p not in env:
      Pathlist.append(p)
  return(Pathlist)

def addPath(Paths:list, env, ignoreRegex=False):
  #Replace absolute Paths prefixes with wildcards
  if ignoreRegex == False:
    env = [sub.replace('C:\WINDOWS', '%SystemRoot%') for sub in env]
    env = [(re.sub(r'(.*)\\Users\\(.*)\\AppData',"%USERPROFILE%\\\\AppData",x)) for x in env]
    for Path in Paths:
      env.append(Path)
    env = sorted([*set(env)])
    env = ';'.join(env)
    var = "Path"
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

#checks if Compass and MongoDB are in Path, if not install them
def setPath(files=('mongodb','mongosh','compass','node','vscode')):
  env = str(os.getenv('Path')).split(';')
  env = [x for x in env if x != '']
  Paths = []
  for file in files:
    Paths.append(selectPath(file))
  Paths = checkPath(Paths,env)
  if len(Paths) > 0:
    print(str(len(Paths))+' file(s) not in Path')
    for p in Paths:
      print(p)
    addPath(Paths, env)