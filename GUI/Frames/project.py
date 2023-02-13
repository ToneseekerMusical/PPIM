import customtkinter as ctk
from Controllers.Mongo import MongoDB

class ProjectFrame(ctk.CTkFrame):
  def __init__(self,client:MongoDB,site:str,*args,**kwargs):
    super().__init__(
      bg_color='transparent',
      fg_color='transparent',
      *args,
      **kwargs
      )
    self.site = client.Connect(dbName=site)
    self.siteData = self.site.get_collection('Site Info').find_one()

    self.title = ctk.CTkLabel(self,text=self.siteData['_id'],font=ctk.CTkFont(size=20,weight="bold"))
    self.title.grid(row=0,column=0,sticky='nsew')