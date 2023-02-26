import customtkinter as ctk
from GUI.Frames.NewProjectFrames.NewProjectGithub import GithubFrame as Github
from GUI.Frames.NewProjectFrames.NewProjectFrontendInfo import FrontendFrame as Frontend
from GUI.Frames.NewProjectFrames.NewProjectPlugins import PluginFrame as Plugins
from GUI.Frames.NewProjectFrames.NewProjectInfo import ProjectFrame as Project
from GUI.Frames.NewProjectFrames.NewProjectBackendInfo import BackendFrame as Backend
from Controllers.Mongo import MongoDB
from Controllers.SiteManagement import SiteManagement
from pymongo.database import Database
from pathlib import Path
import threading

class NewProjectFrame(ctk.CTkFrame):
  def __init__(self,client:MongoDB,PPIM:Database,*args,**kwargs):
    super().__init__(
      bg_color='transparent',
      fg_color='transparent',
      *args,
      **kwargs
      )
    
    self.client = client
    self.PPIM = PPIM
    self.githubUser = 'Username'
    self.versions = PPIM.get_collection('System').find_one()
    self.mongoDBVersions = list(self.versions['Dependencies']['MongoDB'].keys())[:-2]
    self.nodeVersions = list(self.versions['Dependencies']['NodeJS'].keys())[:-2]
    self.plugins = ['Auth0','Blurhash','Cloud-Storage','Cloudinary','Default-Roles',
      'Form-Builder','Google-One-Tap','Hash-Upload','Image-Kit','Lexical','NestedDocs',
      'oAuth','Phone-Field','Redis-Cache','S3-Upload','Search','SEO','Stripe','webP',
      'Zapier','Redirects','Base-64','Password-Protection','Resolve-Alias','Tenancy']
    self.payloadVersions = ['1.6.10','1.6.9','1.6.8','1.6.7']

    self.frontendTemplates = ['create-react-app','create-react-native-app','create-next-app','create-vite-app']
    self.adminTemplates = ['None','Payload Admin',]

    self.grid_columnconfigure((0,1), minsize=400, weight=1)  # configure grid of individual tabs
    self.grid_rowconfigure((0,1,2,3), weight=1)  # configure grid of individual tabs
    self.grid_rowconfigure((4,5), weight=1)  # configure grid of individual tabs

    self.title = ctk.CTkLabel(self,text='Add New Site',font=ctk.CTkFont(size=20,weight="bold"))
    self.title.grid(row=0,column=0,columnspan=2,sticky='ew')

    self.githubInfo = Github(self.githubUser,self)
    self.githubInfo.grid(row=1,column=1,padx=(5,10),sticky='ew')

    self.frontendInfo = Frontend(self.nodeVersions,self.payloadVersions,self.frontendTemplates,self.adminTemplates,self)
    self.frontendInfo.grid(row=2,column=0,padx=5,sticky='ew')

    self.backendInfo = Backend(self.mongoDBVersions,self)
    self.backendInfo.grid(row=2,column=1,padx=(5,10),sticky='ew')

    self.projectInfo = Project(self.backendInfo, self.githubInfo, self.githubUser, self)
    self.projectInfo.grid(row=1,column=0,padx=5,sticky='ew')

    self.plugins = Plugins(self.plugins,self)
    self.plugins.grid(row=3,column=0,columnspan=2,padx=(5,10),pady=5,sticky='ew')
    
    self.newsite = ctk.CTkButton(self,text='Create New Site',command=threading.Thread(target = self.createNewPayloadSite).start)
    self.newsite.grid(row=4,rowspan=2,column=1,padx=(5,10),pady=(5,10),sticky='nsew')

    self.progress = ctk.CTkProgressBar(self,mode='indeterminate')
    self.progress.grid(row=4,column=0,padx=5,pady=5,sticky='sew')

    self.readout = ctk.CTkLabel(self,text='installation progress readout')
    self.readout.grid(row=5,column=0,pady=(0,10),sticky='nsew')
  
  def createNewPayloadSite(self):
    field:ctk.CTkBaseClass | ctk.CTkCheckBox
    document = {'siteConfig':{},'github':{},'frontend':{},'plugins':{},'backend':{}}
    
    for name, field in self.projectInfo.inputs.items():
      if type(field) == ctk.CTkLabel:
        document['siteConfig'][name] = str(Path(f'{Path().cwd()}{field.cget("text")}'))
        document['frontend']['frontendPath'] = str(Path(f'{Path().cwd()}{field.cget("text")}\\frontend'))
        document['frontend']['adminPath'] = str(Path(f'{Path().cwd()}{field.cget("text")}\\admin'))
      if type(field) == ctk.CTkEntry and name == 'siteName':
        document['_id'] = f'{field.get().replace(" ","-")}'
        document['backend']['databaseName'] = f'{field.get().replace(" ","-")}'
        document['siteConfig'][name] = f'{field.get()}'
      if type(field) == ctk.CTkEntry:
        document['siteConfig'][name] = field.get()
    
    for name, field in self.githubInfo.inputs.items():
      if type(field) not in (ctk.CTkLabel, ctk.CTkSwitch):
        document['github'][name] = field.get()
      if type(field) == ctk.CTkLabel:
        document['github'][name] = field.cget('text')
    
    for name, field in self.frontendInfo.tabs['frontendConfig']['inputs'].items():
      document['frontend'][name] = field.get()
      if name == 'frontendPort':
        document['frontend'][name] = 3001
      if name == 'adminPort':
        document['frontend'][name] = 3000
    document['frontend']['frontendHost'] = 'http://localhost'
    document['frontend']['adminHost'] = 'http://localhost'
    for name, field in self.plugins.inputs.items():
      document['plugins'][name] = {}
      document['plugins'][name]['enabled'] = field.get()
    
    for name, field in self.backendInfo.tabs['backendConfig']['inputs'].items():
      if type(field) == ctk.CTkLabel and name != 'databaseName':
        document['backend'][name] = f'{field.cget("text")}'
      if type(field) not in (ctk.CTkSwitch, ctk.CTkLabel) :
        document['backend'][name] = field.get()
    if self.backendInfo.tabs['Edit']['inputs']['username'].get() != '':
      document['backend']['username'] = self.backendInfo.tabs['Edit']['inputs']['username'].get()
    else:
      document['backend']['username'] = ''
    if self.backendInfo.tabs['Edit']['inputs']['password'].get() != '':
      document['backend']['password'] = self.backendInfo.tabs['Edit']['inputs']['password'].get()
    else:
      document['backend']['password'] = ''

    site = SiteManagement(self.PPIM,self.client)
    site.CreateSiteDB(document)
    self.readout.configure(text=site.output)
    self.grid_remove()
    return document['_id']
    