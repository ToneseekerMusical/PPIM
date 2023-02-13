from pathlib import Path
from pymongo.database import Database
from Controllers.Mongo import MongoDB
import subprocess

class SiteManagement():
  def __init__(self,PPIM:Database,client:MongoDB,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.PPIM = PPIM
    self.client = client

  def CreateSiteDB(self,document):
    try:
      self.PPIM.create_collection('Sites',check_exists=True)
      self.PPIM.get_collection('Sites').insert_one(document)
    except:
      try:self.PPIM.get_collection('Sites').insert_one(document)
      except:pass
    try:
      newDB = self.client.Connect(dbName=document['_id'])
      newDB.create_collection('SiteInfo',check_exists=True,capped=True,max=1,size=52428800)
      newDB.get_collection('SiteInfo').insert_one(document)
    except:
      try:
        newDB = self.client.Connect(dbName=document['_id'])
        newDB.get_collection('SiteInfo').insert_one(document)
      except:
        pass
    self.__CreateDirectory(document)

  def DeleteSiteDB(self):...

  def __CreateDirectory(self,document:dict):
    path = document['siteConfig']['dirPath']
    path = Path(path)
    locations = {'admin': f'{path}\\admin'}
    plugins = document['plugins']
    Path(f'{path}/admin').mkdir(parents=True)
    if document['frontend']['frontendTemplate'] != 'None':
      Path(f'{path}/frontend').mkdir()
      locations['frontend'] = f'{path}\\frontend'
    print(document['frontend']['adminTemplate'])
    if document['frontend']['adminTemplate'] == 'None':
      self.__NPMInstall(document['_id'],locations,plugins)
    else:
      self.__DownloadTemplates()

  def __DownloadTemplates(self):...

  def __NPMInstall(self,name:str,locations:dict,plugins:dict):
    for location, path in locations.items():
      p = f'{Path(path)}'
      if location == 'admin':
        payload = subprocess.Popen(['powershell.exe','npx','create-payload-app'],cwd=p,stdin=subprocess.PIPE)
        #payload.communicate(f'{name}')
        #payload.communicate(f'mongodb://localhost:27017/{name}')

  def __DeleteDirectory(self):...
  
  def __UploadToGithub(self):...
  
  def Deploy(self):...