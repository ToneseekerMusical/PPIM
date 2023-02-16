import Controllers.System as System
import subprocess, pymongo, psutil
from subprocess import Popen, run
import pymongo.database as database

class MongoDB():
  def __init__(self, *args, **kwargs):
    super().__init__(*args,**kwargs)
    self.adminDB = ('PPIM', 'admin', 'config', 'local')

  def mongoStatus(self):
    status = psutil.win_service_get('mongoDB').status()
    return status
  #If service is stopped, start it
  def StartService(self):
    if System.get_service('MongoDB')['status'] == 'stopped':
      System.runAsAdmin(['net','start','MongoDB'])

  #If service is running, shut it down
  def StopService(self):
    if System.get_service('MongoDB')['status'] == 'running':
      System.runAsAdmin(['net','stop','MongoDB'])

  #Connects to the server with a short timeout set to
  #verify that the server is running or reachable
  def __TestConnect(self,conStr):
    with pymongo.timeout(1):
      try:
        return pymongo.MongoClient(conStr)
      except Exception as e:
        raise e

  #Sends the connection string to the object for later use.
  #Tests connection to server and sends the server to the object
  #If connection passes, sends the database to the object.
  #If no database name is specified, returns a filtered list of databases
  #if connection string is specified, sends the database to the object
  def Connect(self,conStr:str='',dbName:str=''):
    if not hasattr(self, 'server') and conStr == '':
      raise Exception('You must first initialize the database with a connection string!')
    if not hasattr(self,'server') and conStr != '' and dbName == '':
      self.conStr = conStr
      self.server = self.__TestConnect(conStr)
    if self.server != None:
      if dbName != '':
        if self.server == None: raise Exception('Error connecting to the server!')
        return self.server[dbName]
      elif dbName == '':
        self.dbList = [x for x in self.server.list_database_names() if x not in self.adminDB]

  def RefreshServer(self):
    self.dbList = [x for x in self.server.list_database_names() if x not in self.adminDB]

  #Checks if database already exists, if not, checks if new name is valid.
  #Checks name, if valid, creates the databas with site info collection
  def CreateDatabase(self,dbName:str):
    if dbName in self.dbList: raise Exception('Database already Exists! Please choose another name.')
    if database._check_name(dbName) is not None: Exception('Database name is invalid! Please choose another name.')
    db = self.server[dbName]
    database.Database.create_collection(db,'Site Info',check_exists=True,capped=True,max=1,size=52428800)
    self.dbList.append(dbName)

  #Checks if the old or new name is an admin database, if not, updates the object's
  #database list. Checks if a database already exists that matches the new name,
  #If not, dumps the database to PPIM/dump/ and restores it with the new name.
  def RenameDatabase(self,oldName:str,newName:str):
    if oldName in self.adminDB: raise Exception('Cannot rename admin database.')
    if newName in self.adminDB: raise Exception('Cannot rename database to reserved name.')
    self.dbList = [x for x in self.server.list_database_names() if x not in self.adminDB]
    if newName in self.dbList: raise Exception('Cannot Rename! A database with that name already exists.')
    run(f'powershell.exe mongodump --archive="{oldName}-archive" --db={oldName}')
    run(f'powershell.exe mongorestore --archive="{oldName}-archive" --nsFrom=\'{oldName}.*\' --nsTo=\'{newName}.*\'')
    self.server.drop_database(oldName)

  #Checks if database is not an admin database
  #If not, updates the database list and checks if
  #the database exists, if it does, drop it.
  def DeleteDatabase(self,dbName:str):
    if dbName in self.adminDB: raise Exception('Admin database cannot be deleted')
    self.dbList = [x for x in self.server.list_database_names() if x not in self.adminDB]
    if dbName not in self.dbList: raise Exception('Database doesn\'nt exist')
    self.server.drop_database(dbName)

class MongoCompass():
  def __init__(name,*args,**kwargs):
    super().__init__()

  #Starts Compass
  def startCompass(constr):
    print(constr)
    Popen(['mongodbcompass',constr])

class MongoSH():
  def __init__(db, *args,**kwargs):
    super().__init__()

  def startMongosh(constr):
    Popen(['mongosh',constr],creationflags=subprocess.CREATE_NEW_CONSOLE)