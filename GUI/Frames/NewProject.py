import customtkinter as ctk
from GUI.Frames.NewProjectFrames.NewProjectGithub import githubFrame as Github
from GUI.Frames.NewProjectFrames.NewProjectFrontendInfo import frontendFrame as Frontend
from GUI.Frames.NewProjectFrames.NewProjectPlugins import pluginFrame as Plugins
from GUI.Frames.NewProjectFrames.NewProjectInfo import projectFrame as Project
from GUI.Frames.NewProjectFrames.NewProjectBackendInfo import BackendFrame as Backend
from Controllers.Mongo import MongoDB
from Controllers.SiteManagement import SiteManagement
from pymongo.database import Database
from pathlib import Path

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
    self.versions = PPIM.get_collection('System').find_one()
    self.mongoDBVersions = list(self.versions['Dependencies']['MongoDB'].keys())[:-2]
    self.nodeVersions = list(self.versions['Dependencies']['NodeJS'].keys())[:-2]
    self.plugins = ['Cloud-Storage','SEO','Form-Builder','S3-Upload','Lexical','Search',
      'webP','Blurhash','Stripe','Auth0','Cloudinary','NestedDocs','Hash-Upload','oAuth',
      'Image-Kit','Redis-Cache','Zapier','Google-One-Tap','Phone-Field','Default-Roles'
    ]

    self.frontendTemplates = ['create-react-app','create-react-native-app','create-next-app','create-vite-app']
    self.adminTemplates = ['None','Payload Admin',]

    self.grid_columnconfigure((0,1,2), weight=1)  # configure grid of individual tabs
    self.grid_rowconfigure((0,1), weight=0)  # configure grid of individual tabs
    self.grid_rowconfigure(2, weight=1)  # configure grid of individual tabs

    #Create Github Frame
    self.github = Github(self)
    self.github.grid(row=0,column=1,padx=5,sticky='ew')

    #Create MongoDB Frame
    self.frontendInfo = Frontend(self.nodeVersions,self.frontendTemplates,self.adminTemplates,self)
    self.frontendInfo.grid(row=0,column=2,padx=(5,10),sticky='ew')

    #Create MongoDB Frame
    self.backendInfo = Backend(self.mongoDBVersions,self)
    self.backendInfo.grid(row=1,rowspan=2,column=2,padx=(5,10),pady=(0,5),sticky='new')

    #Create Project Frame
    self.projectInfo = Project(self.backendInfo, self)
    self.projectInfo.grid(row=0,column=0,padx=5,sticky='ew')

    #Create Plugin Frame
    self.plugins = Plugins(self.plugins,self)
    self.plugins.grid(row=1,column=0,columnspan=2,padx=5,pady=(0,10),sticky='nsew')
    
    self.newsite = ctk.CTkButton(self,text='Create New Site',command=self.createNewPayloadSite)
    self.newsite.grid(row=3,column=2,padx=(5,10),pady=(5,10),sticky='nsew')

    self.progress = ctk.CTkProgressBar(self,mode='indeterminate')
    self.progress.grid(row=2,column=0,columnspan=2,padx=5,sticky='sew')

    self.readout = ctk.CTkLabel(self,text='installation progress readout')
    self.readout.grid(row=3,column=0,columnspan=2,pady=(0,10),sticky='ew')
  
  def createNewPayloadSite(self):
    field:ctk.CTkBaseClass | ctk.CTkCheckBox
    document = {'siteConfig':{},'github':{},'frontend':{},'plugins':{},'backend':{}}
    for name, field in self.projectInfo.inputs.items():
      if type(field) == ctk.CTkLabel:
        document['siteConfig'][name] = f'{Path().cwd()}{field.cget("text")}'
      if type(field) == ctk.CTkEntry and name == 'siteName':
        document['_id'] = f'{field.get().replace(" ","-")}'
        document['backend']['databaseName'] = f'{field.get().replace(" ","-")}'
        document['siteConfig'][name] = f'{field.get()}'
      if type(field) == ctk.CTkEntry:
        document['siteConfig'][name] = field.get()
    for name, field in self.github.inputs.items():
      if type(field) != ctk.CTkLabel:
        document['github'][name] = field.get()
    for name, field in self.frontendInfo.inputs.items():
      document['frontend'][name] = field.get()
    for name, field in self.plugins.inputs.items():
      document['plugins'][name]['enabled'] = field.get()
    for name, field in self.backendInfo.inputs.items():
      if type(field) == ctk.CTkLabel and name != 'databaseName':
        document['backend'][name] = f'{field.cget("text")}'
      if type(field) not in (ctk.CTkSwitch, ctk.CTkLabel) :
        document['backend'][name] = field.get()
    site = SiteManagement(self.PPIM,self.client)
    site.CreateSiteDB(document)
    self.grid_remove()
    return document['_id']
    