import customtkinter as ctk
from Controllers.Mongo import MongoDB
from pymongo.database import Database
from GUI.Frames.ProjectFrames.ProjectInfo import projectInfo
from GUI.Frames.ProjectFrames.PluginManagement import pluginManager
from GUI.Frames.ProjectFrames.DBInfo import databaseInfo
from GUI.Frames.ProjectFrames.EditSite import siteSetup
from GUI.Frames.ProjectFrames.DevTools import devTools
from GUI.Frames.ProjectFrames.Github import Github

class ProjectFrame(ctk.CTkFrame):
  def __init__(self,client:MongoDB,site:str,*args,**kwargs):
    super().__init__(
      bg_color='transparent',
      fg_color='transparent',
      *args,
      **kwargs
      )

    self.grid_columnconfigure((0,1),uniform='True',weight=1)

    self.site:Database = client.Connect(dbName=site)
    self.siteData = self.site.get_collection('Site Info').find_one()
    
    self.title = ctk.CTkLabel(self,text=self.siteData['_id'],font=ctk.CTkFont(size=20,weight="bold"),anchor='center')
    self.title.grid(row=0,column=0,columnspan=2,pady=(10,0),sticky='nsew')

    self.projectInfo = projectInfo(self.siteData['frontend'],self.site,self.siteData['_id'],self)
    self.projectInfo.grid(row=1,column=0,sticky='ew')

    self.plugins = pluginManager(self.siteData['plugins'],self)
    self.plugins.grid(row=2,column=0,rowspan=3,sticky='nsew',pady=(0,10))

    self.dbInfo = databaseInfo(self.siteData['backend'],self)
    self.dbInfo.grid(row=1,column=1,sticky='ew',padx=10)

    self.editSite = siteSetup(self)
    self.editSite.grid(row=2,column=1,sticky='ew',padx=10)

    self.devTools = devTools(self.siteData['frontend'],self)
    self.devTools.grid(row=3,column=1,sticky='ew',padx=10,pady=(0,10))
    
    self.devTools = Github(self)
    self.devTools.grid(row=4,column=1,sticky='ew',padx=10,pady=(0,10))