import ctypes
from pathlib import Path as Path
from Controllers.Mongo import MongoDB
import Controllers.System as System
from Controllers.Dependencies import Dependencies
from Controllers.System import runAsAdmin

class Setup():
  def __init__(self, phase:str, installPath="", mongoVer='base'):
    if phase.lower() not in ('install', 'config', 'add', 'check', 'update'): raise Exception('You must specify whether this is an installation or update.')
    self.__mongoVer = mongoVer
    self.__phase = phase
    if installPath != "":
      self.__instPath = Path(installPath)
    else:
      self.__instPath = Path.cwd()

  def Install(self):
    downloadDeps = Dependencies(self.__mongoVer,self.__phase,self.__instPath)
    mongoV = list(downloadDeps.allDependencies['MongoDB'].keys())[0]
    cfgPath = Path(f'{self.__instPath}\lib\MongoDB\{mongoV}\\bin\mongod.conf')

    srv = Path(f'{self.__instPath}\srv\mongodb')
    cfgTemplate = Path(f'{self.__instPath}\mongod.conf.template')

    if not srv.is_dir(): srv.mkdir(parents=True)
    confc = open(cfgTemplate,'r').read()
    confc = confc.replace('<logpath>',f'{srv}\mongo.log')
    confc = confc.replace('<PIDPath>',f'{srv}\mongo.pid')
    confc = confc.replace('<TzDBPath>',f'{srv}')
    confc = confc.replace('<storagepath>',f'{srv}')

    Path(cfgPath).touch()
    conff = open(cfgPath,'w')
    conff.write(confc)
    conff.close()

    Path(f'{srv}\mongod.pid').touch()
    Path(f'{srv}\mongod.log').touch()
    Path(f'{self.__instPath}\websites').touch()

    if not System.get_service('MongoDB'):
      ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",
        "powershell.exe",
        f"""
        mongod --config {cfgPath} --install --serviceName MongoDB;
        net start MongoDB
        """,
        None,
        0
      )
    
  def Config(self):
    dependencies = Dependencies(self.__mongoVer,'config',self.__instPath)
    dependencies = dependencies.allDependencies

    

    ver = '0.0.01dev'

    db = MongoDB()
    db.StartService()
    db.Connect(
    "mongodb://localhost:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=PPIM"
    )
    db = db.Connect(dbName='PPIM')
    sys = {
      'Version': ver,
      'Dependencies': dependencies
    }
    try:
      self.__system = db.create_collection('System',check_exists=True,capped=True,max=1,size=52428800)
      db.create_collection('Settings',check_exists=True,capped=True,max=1,size=52428800)
    except:
      self.__system = db.get_collection('System')
      self.__system.insert_one(sys)