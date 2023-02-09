import ctypes
from pathlib import Path as Path
from Controllers.Mongo import MongoDB
import Controllers.System as System
from Controllers.Dependencies import Dependencies
from Controllers.System import runAsAdmin

class Setup():
  def __init__(self, phase:str, installPath="", mongoVer='base'):
    self.__ver = '0.0.01dev'
    self.__mongoVer = mongoVer
    self.__phase = phase
    if installPath != "":
      self.__instPath = Path(installPath)
    else:
      self.__instPath = Path.cwd()

  def StartSetup(self):
    self.__downloadDeps = Dependencies(self.__mongoVer,self.__phase,self.__instPath)
    self.__dependencies = self.__downloadDeps.allDependencies
    self.__mongoV = list(self.__dependencies['MongoDB'].keys())[0]

    self.__srv = Path(f'{self.__instPath}\srv\mongodb')
    self.__mdbCfgTemplate = Path(f'{self.__instPath}\mongodb.conf.template')
    self.__mdbCfgPath = Path(f'{self.__instPath}\lib\mongodb\{self.__mongoV}\\bin\mongodb.conf')

    if not self.__srv.is_dir(): self.__srv.mkdir(parents=True)
    confc = open(self.__mdbCfgTemplate,'r').read()
    confc = confc.replace('<logPath>',f'{self.__srv}\mongo.log')
    confc = confc.replace('<PIDPath>',f'{self.__srv}\mongo.pid')
    confc = confc.replace('<TzDBPath>',f'{self.__srv}')
    confc = confc.replace('<storagePath>',f'{self.__srv}')
    conff = open(self.__mdbCfgPath,'w')
    conff.write(confc)
    conff.close()

    Path(f'{self.__srv}\mongod.pid').touch()
    Path(f'{self.__srv}\mongod.log').touch()
    if self.__phase == 'config':
      if not System.get_service('MongoDB'):
        print('trying to create system service')
        print(self.__mdbCfgPath)
        #runAsAdmin(['mongod', '--config', self.__mdbCfgPath, '--install' '--serviceName' 'MongoDB'])
        ctypes.windll.shell32.ShellExecuteW(
          None,
          "runas",
          "powershell.exe",
          f"""
          f'mongod.exe --config {self.__mdbCfgPath} --install --serviceName MongoDB'
          """,
          None,
          0
        )
      db = MongoDB()
      db.StartService()
      print(db.server)
      db = db.Connect(
      "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=PPIM",
      "PPIM"
      )
      self.__sys = {
        'Version': self.__ver,
        'Dependencies': self.__dependencies
      }
      try:
        self.__system = db.create_collection('System',check_exists=True,capped=True,max=1,size=52428800)
        self.__settings = db.create_collection('Settings',check_exists=True,capped=True,max=1,size=52428800)
      except:
        self.__system = db.get_collection('System')
      try:
        self.__system.insert_one(self.__sys)
      except:
        pass