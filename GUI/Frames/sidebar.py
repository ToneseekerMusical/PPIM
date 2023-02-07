import customtkinter as ctk
import GUI.Frames.Sidebar.Update as Updates
import GUI.Frames.Sidebar.Mongo as Mongo

class SidebarFrame(ctk.CTkFrame):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
        # create sidebar frame with widgets
    self.columnconfigure(0,weight=1)
    self.rowconfigure(0, weight=1)
    self.rowconfigure(1, weight=0)

    self.mongo = Mongo.MongoFrame(
      self
    )
    self.mongo.grid(
      row=0,
      column=0,
      sticky='new'
    )

    self.updates = Updates.updateFrame(
      self
    )
    self.updates.grid(
      row=1,
      column=0,
      sticky='sew'
    )