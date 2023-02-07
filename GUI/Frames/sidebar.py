import customtkinter as ctk
import GUI.Frames.Sidebar.Update as Updates
import GUI.Frames.Sidebar.Mongo as Mongo

class SidebarFrame(ctk.CTkFrame):
  def __init__(self,*args,**kwargs):
    super().__init__(
      bg_color='transparent',
      fg_color='transparent',
      *args,
      **kwargs
      )

    self.columnconfigure(0,weight=0)
    self.rowconfigure((0,2), weight=1)
    self.rowconfigure(1, weight=0)

    self.mongo = Mongo.MongoFrame(
      self
    )
    self.mongo.grid(
      row=0,
      column=0,
      sticky='n'
    )

    self.updates = Updates.updateFrame(
      self
    )
    self.updates.grid(
      row=2,
      column=0,
      sticky='s',
    )