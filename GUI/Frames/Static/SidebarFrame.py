import customtkinter as ctk
from GUI.Frames.Sidebar import SiteManagementFrame
from GUI.Frames.Sidebar import MongoFrame
from GUI.Frames.Sidebar import OptionsFrame
from Controllers.Mongo import MongoDB
from pymongo.database import Database

class SidebarFrame(ctk.CTkFrame):
  def __init__(self,client:MongoDB,PPIM:Database,*args,**kwargs):
    super().__init__(bg_color='transparent',fg_color='transparent',width = 200,*args,**kwargs)

    self.rowconfigure((0,2), weight=1)
    self.rowconfigure(1, weight=0)

    self.mongo = MongoFrame(client,self)
    self.mongo.grid(padx=0,row=0,column=0,sticky='nw')

    self.sites = SiteManagementFrame(self.master,client,PPIM,self,)
    self.sites.grid(padx=0,row=1,column=0,sticky='nsew')

    self.options = OptionsFrame(PPIM,self)
    self.options.grid(padx = 0,row=2,column=0,sticky='sw',)