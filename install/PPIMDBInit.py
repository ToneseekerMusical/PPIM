from pathlib import Path as Path
import ctypes
import Controllers.Mongo as Mongo
import pymongo.database as Database
import json
import Controllers.System as System

def PPIMdbSetup():
  cwd = str(Path.cwd())
  srv = Path(cwd+'\\srv\\mongodb')
  conft = Path(cwd+'\\Install\\mongod.conf')
  conf = Path(cwd+'\\lib\\mongodb\\bin\\mongod.conf')
  
  if srv.is_dir() == False: srv.mkdir(parents=True)
  
  confc = open(conft,'r').read()
  confc = confc.replace('<logpath>',str(srv)+'\\mongo.log')
  confc = confc.replace('<PIDPath>',str(srv)+'\\mongo.pid')
  confc = confc.replace('<TzDBPath>',str(srv))
  confc = confc.replace('<storagepath>',str(srv))
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
  system.insert_one(sysinf)