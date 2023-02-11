import customtkinter as ctk
from GUI.Frames.Sidebar.Options import OptionsFrame
from GUI.Frames.Sidebar.Mongo import MongoFrame
from GUI.Frames.Sidebar.SiteControl import SiteControl

class SidebarFrame(ctk.CTkFrame):
  def __init__(self,client,*args,**kwargs):
    super().__init__(
      bg_color='transparent',
      fg_color='transparent',
      *args,
      **kwargs
      )

    self.columnconfigure(0,weight=0)
    self.rowconfigure((0,2), weight=1)
    self.rowconfigure(1, weight=0)

    self.mongo = MongoFrame(
      client,
      self
    )
    self.mongo.grid(
      row=0,
      column=0,
      sticky='n'
    )

    self.sites = SiteControl(
      client,
      self.master,
      self,
    )
    self.sites.grid(
      row = 1,
      column = 0,
      sticky = 'nsew'
    )
    self.updates = OptionsFrame(
      self
    )
    self.updates.grid(
      row=2,
      column=0,
      sticky='s',
    )