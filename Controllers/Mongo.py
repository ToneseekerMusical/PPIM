import pathlib, psutil, ctypes, sys, Controllers.System
from subprocess import Popen, run

def get_service(name):
  service = None
  try:
    service = psutil.win_service_get(name)
    service = service.as_dict()
  except:
    pass
  return service

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

#Checks if database folder exists, if not, creates it
#and starts MongoDB
#Need to add password settings!
def firststartDB():
  path = pathlib.Path
  cwd = str(path.cwd())
  mongod = path(cwd+'\\lib\\mongodb\\bin\\')
  srv = path(cwd+'\\srv\\mongodb')
  conft = path(cwd+'\\Install\\mongod.conf')
  conf = path(cwd+'\\lib\\mongodb\\bin\\mongod.conf')
  if srv.is_dir() == False:
      srv.mkdir(parents=True)
  confc = open(conft,'r').read()
  confc = confc.replace('<logpath>',str(srv)+'\\mongo.log')
  confc = confc.replace('<PIDPath>',str(srv)+'\\mongo.pid')
  confc = confc.replace('<TzDBPath>',str(srv))
  confc = confc.replace('<storagepath>',str(srv))
  try:
    logf = open(str(path(cwd+'\\srv\\mongodb\\mongo.log')),'w')
    logf.close()
  except:
     pass
  conff = open(conf,'w')
  conff.write(confc)
  conff.close()
  path(str(srv)+'\\mongod.pid').touch()
  Controllers.System.runAsAdmin(['mongod', '--config', str(conf), '--install','--serviceName','MongoDB'])
  Controllers.System.runAsAdmin(['net','start','MongoDB'])
  
def startDB():
  if get_service('MongoDB')['status'] == 'stopped':
    Controllers.System.runAsAdmin(['net','start','MongoDB'])

#Cannot Shut Down MongoDB at this time
def stopDB():
  if get_service('MongoDB')['status'] == 'running':
    Controllers.System.runAsAdmin(['net','stop','MongoDB'])

#Starts Compass
def startCompass():
   Popen('mongodbcompass.exe')