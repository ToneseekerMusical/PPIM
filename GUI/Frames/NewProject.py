import customtkinter as ctk
from GUI.Frames.NewProjectFrame.NewProjectGithub import githubFrame as Github
from GUI.Frames.NewProjectFrame.NewProjectFrontendInfo import frontendFrame as Frontend
from GUI.Frames.NewProjectFrame.NewProjectPlugins import pluginFrame as Plugins
from GUI.Frames.NewProjectFrame.NewProjectInfo import projectFrame as Project
from GUI.Frames.NewProjectFrame.NewProjectBackendInfo import BackendFrame as Backend
from GUI.Frames.Shell import shellFrame
from pathlib import Path

class NewProjectFrame(ctk.CTkFrame):
  def __init__(self,*args,**kwargs):
    super().__init__(
      bg_color='transparent',
      fg_color='transparent',
      *args,
      **kwargs
      )
    
    self.plugins = ['Cloud-Storage','SEO','Form-Builder','S3-Upload','Lexical','Search',
      'webP','Blurhash','Stripe','Auth0','Cloudinary','NestedDocs','Hash-Upload','oAuth',
      'Image-Kit','Redis-Cache','Zapier','Google-One-Tap','Phone-Field','Default-Roles'
    ]

    self.feTemplates = ['Payload Website']
    self.beTemplates = ['Payload Admin']
    self.nodeVersions = ['v18.12.1']
    self.mongoDBVersion = ['6.0.4']

    self.grid_columnconfigure((0,1,2), weight=1)  # configure grid of individual tabs
    self.grid_rowconfigure((0,1), weight=0)  # configure grid of individual tabs
    self.grid_rowconfigure(2, minsize=0, weight=1)  # configure grid of individual tabs

    #Create Github Frame
    self.github = Github(self)
    self.github.grid(row=0,column=1,padx=5,sticky='ew')

    #Create MongoDB Frame
    self.frontendInfo = Frontend(self.nodeVersions,self.feTemplates,self.beTemplates,self)
    self.frontendInfo.grid(row=0,column=2,padx=(5,10),sticky='ew')

    #Create MongoDB Frame
    self.backendInfo = Backend(self.mongoDBVersion,self)
    self.backendInfo.grid(row=1,rowspan=2,column=2,padx=(5,10),pady=(0,5),sticky='new')

    #Create Project Frame
    self.projectInfo = Project(self.backendInfo, self)
    self.projectInfo.grid(row=0,column=0,padx=5,sticky='ew')

    #Create Plugin Frame
    self.plugins = Plugins(self.plugins,self)
    self.plugins.grid(row=1,column=0,columnspan=2,padx=5,pady=(0,10),sticky='nsew')
    
    self.newPayloadButton = ctk.CTkButton(
      self,
      text='Create New Site',
      command=self.createNewPayloadSite
      )
    self.newPayloadButton.grid(
      row=3,
      column=2,
      padx=(5,10),
      pady=(5,10),
      sticky='nsew'
      )

    self.progress = ctk.CTkProgressBar(
      self,
      mode='indeterminate'
    )
    self.progress.grid(
      row=2,
      column=0,
      columnspan=2,
      padx=5,
      sticky='sew'
    )

    self.readout = ctk.CTkLabel(
      self,
      text='installation progress readout'
    )
    self.readout.grid(
      row=3,
      column=0,
      columnspan=2,
      pady=(0,10),
      sticky='ew'
    )
    # set default values
    #only enable button when  
    #self.newPayloadButton.configure(state='disabled')
  
  def createNewPayloadSite(self):
    field:ctk.CTkBaseClass | ctk.CTkCheckBox
    document = {'siteConfig':{},'github':{},'frontend':{},'plugins':{},'backend':{}}
    for name, field in self.projectInfo.inputs.items():
      if type(field) == ctk.CTkLabel:
        document['siteConfig'][name] = f'{Path().cwd()}{field.cget("text")}'
      if type(field) == ctk.CTkEntry:
        document['siteConfig'][name] = field.get()
    for name, field in self.github.inputs.items():
      if type(field) != ctk.CTkLabel:
        document['github'][name] = field.get()
    for name, field in self.frontend.inputs.items():
      document['frontend'][name] = field.get()
    for name, field in self.plugins.inputs.items():
      document['plugins'][name] = field.get()
    
    print(document)