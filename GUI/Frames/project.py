import customtkinter as ctk
from Controllers.Mongo import MongoDB
from GUI.Frames.ProjectFrames.ProjectInfo import projectInfo
from GUI.Frames.ProjectFrames.PluginManagement import pluginManager
from GUI.Frames.ProjectFrames.DBInfo import databaseInfo
from GUI.Frames.ProjectFrames.EditSite import siteSetup
from GUI.Frames.ProjectFrames.DevTools import devTools

class ProjectFrame(ctk.CTkFrame):
  def __init__(self,client:MongoDB,site:str,*args,**kwargs):
    super().__init__(
      bg_color='transparent',
      fg_color='transparent',
      *args,
      **kwargs
      )

    self.grid_rowconfigure((0,1), weight=0)  # configure grid of individual tabs
    self.grid_rowconfigure(2, weight=1)  # configure grid of individual tabs

    self.site = client.Connect(dbName=site)
    self.siteData = self.site.get_collection('Site Info').find_one()

    self.title = ctk.CTkLabel(self,text=self.siteData['_id'],font=ctk.CTkFont(size=20,weight="bold"),anchor='center')
    self.title.grid(row=0,column=0,columnspan=2,sticky='nsew')

    self.projectInfo = projectInfo(self)
    self.projectInfo.grid(row=1,column=0,sticky='ew')

    self.plugins = pluginManager(self)
    self.plugins.grid(row=2,column=0,rowspan=2,sticky='ew',pady=(0,10))

    self.dbInfo = databaseInfo(self)
    self.dbInfo.grid(row=1,column=1,sticky='ew',padx=10)

    self.editSite = siteSetup(self)
    self.editSite.grid(row=2,column=1,sticky='ew',padx=10)

    self.devTools = devTools(self)
    self.devTools.grid(row=3,column=1,sticky='ew',padx=10,pady=(0,10))