import customtkinter as ctk
from Controllers.Mongo import MongoDB
from pymongo.database import Database
from GUI.Frames.ProjectFrames.InfoFrame import InfoFrame
from GUI.Frames.ProjectFrames.PluginFrame import PluginFrame
from GUI.Frames.ProjectFrames.DBInfoFrame import DBInfoFrame
from GUI.Frames.ProjectFrames.EditSiteFrame import EditSiteFrame
from GUI.Frames.ProjectFrames.DevToolsFrame import DevToolsFrame
from GUI.Frames.ProjectFrames.GithubFrame import GithubFrame

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

    self.projectInfo = InfoFrame(self.siteData['frontend'],self.site,self.siteData['_id'],self)
    self.projectInfo.grid(row=1,column=0,sticky='ew')

    self.plugins = PluginFrame(self.siteData['plugins'],self)
    self.plugins.grid(row=2,column=0,columnspan=2,sticky='nsew',pady=5,padx=(0,10))

    self.dbInfo = DBInfoFrame(self.siteData['backend'],self)
    self.dbInfo.grid(row=1,column=1,sticky='ew',padx=10)

    self.editSite = EditSiteFrame(self)
    self.editSite.grid(row=4,column=0,sticky='ew',pady=(0,10))

    self.devTools = DevToolsFrame(self.siteData['frontend'],self)
    self.devTools.grid(row=3,column=0,sticky='ew')
    
    self.devTools = GithubFrame(self)
    self.devTools.grid(row=3,column=1,sticky='ew',padx=10)