import customtkinter as ctk
from GUI.Frames.Sidebar.Options import OptionsFrame
from GUI.Frames.Sidebar.Mongo import MongoFrame
from GUI.Frames.Sidebar.SiteControl import SiteControl
from Controllers.Mongo import MongoDB

class SidebarFrame(ctk.CTkFrame):
  def __init__(self,client:MongoDB,*args,**kwargs):
    super().__init__(
      bg_color='transparent',
      fg_color='transparent',
      width = 200,
      *args,
      **kwargs
      )

    self.rowconfigure((0,2), weight=1)
    self.rowconfigure(1, weight=0)

    self.mongo = MongoFrame(
      client,
      self
    )
    self.mongo.grid(
      padx=0,
      row=0,
      column=0,
      sticky='nw'
    )

    self.sites = SiteControl(
      self.master,
      client.dbList,
      self,
    )
    self.sites.grid(
      padx=0,
      row=1,
      column=0,
      sticky='w'
    )

    self.options = OptionsFrame(
      self
    )
    self.options.grid(
      padx = 0,
      row=2,
      column=0,
      sticky='sw',
    )