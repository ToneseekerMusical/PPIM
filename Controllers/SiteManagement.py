from pathlib import Path
from pymongo.database import Database
from Controllers.Mongo import MongoDB
import subprocess
import time

class SiteManagement():
  def __init__(self,PPIM:Database,client:MongoDB,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.PPIM = PPIM
    self.client = client
    self.payloadDeps = PPIM.get_collection('System').find_one()
    self.payloadDeps = self.payloadDeps['Dependencies']['NodeJS']
    self.output = None


  def CreateSiteDB(self,document):
    try:
      self.PPIM.create_collection('Sites',check_exists=True)
      self.PPIM.get_collection('Sites').insert_one(document)
    except:
      try:self.PPIM.get_collection('Sites').insert_one(document)
      except:pass
    try:
      newDB = self.client.Connect(dbName=document['_id'])
      newDB.create_collection('Site Info',check_exists=True,capped=True,max=1,size=52428800)
      newDB.get_collection('Site Info').insert_one(document)
    except:
      try:
        newDB = self.client.Connect(dbName=document['_id'])
        newDB.get_collection('Site Info').insert_one(document)
      except:
        pass
    self.__CreateDirectory(document)

  def DeleteSiteDB(self):...

  def __CreateDirectory(self,document:dict):
    self.path = Path(document['siteConfig']['dirPath'])
    self.locations = {'admin': f'{self.path}'}
    self.plugins = document['plugins']
    self.conStr = document['backend']['databaseURI']
    self.nodeVer = document['frontend']['nodeJSversion']
    self.frontend = document['frontend']['frontendTemplate']
    Path(f'{self.path}').mkdir(parents=True)
    if document['frontend']['frontendTemplate'] != 'None':
      Path(f'{self.path}/frontend').mkdir()
      self.locations['frontend'] = f'{self.path}\\frontend'
    if document['frontend']['adminTemplate'] == 'None':
      self.__NPMInstall(document['_id'])
    else:
      self.__DownloadTemplates()

  def __DownloadTemplates(self):...

  def __NPMInstall(self,name:str):
    for location, path in self.locations.items():
      p = f'{Path(path)}'
      if location == 'admin':
        subprocess.run(['powershell.exe','npm','i','create-payload-app'],cwd=p)
        with subprocess.Popen(['powershell.exe','npx','create-payload-app','--name','admin','--template','blank',],
          cwd=p,stdin=subprocess.PIPE, text=True,) as npm:
          npm.stdin.write(f'{self.conStr}\n')
      if location == 'frontend':
        subprocess.Popen(['powershell.exe','npm','i',f'{self.frontend}'],cwd=p)

  def __DeleteDirectory(self):...
  
  def __UploadToGithub(self):...
  
  def Deploy(self):...