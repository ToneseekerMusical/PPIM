import customtkinter as ctk
from GUI.Frames.Settings.Directories import Directories
from GUI.Frames.Settings.Accounts import Accounts
from GUI.Frames.Settings.MongoDB import MongoDB
from GUI.Frames.Settings.NodeJS import NodeJS
from GUI.Frames.Settings.Payload import Payload
from GUI.Frames.Settings.UI import UI
from GUI.Frames.Settings.Updates import Updates

class SettingsFrame(ctk.CTkTabview):
  def __init__(self,PPIM,*args,**kwargs):
    super().__init__(
      fg_color='grey14',
      *args,**kwargs)
    
    self.add('Accounts')
    self.add('Directories')
    self.add('MongoDB')
    self.add('NodeJS')
    self.add('Payload')
    self.add('UI')
    self.add('Updates')
    self.tab('Accounts').grid_columnconfigure(0,weight=1)
    self.tab('Directories').grid_columnconfigure(0,weight=1)
    self.tab('MongoDB').grid_columnconfigure(0,weight=1)
    self.tab('NodeJS').grid_columnconfigure(0,weight=1)
    self.tab('Payload').grid_columnconfigure(0,weight=1)
    self.tab('UI').grid_columnconfigure(0,weight=1)
    self.tab('Updates').grid_columnconfigure(0,weight=1)

    self.accounts = Accounts(PPIM['Accounts'],self.tab('Accounts'))
    self.accounts.grid(column=0,row=0,padx=5,pady=5)
    self.directories = Directories(PPIM['Directories'],self.tab('Directories'))
    self.directories.grid(column=0,row=0,padx=5,pady=5,sticky='ew')
    self.mongodb = MongoDB(PPIM['MongoDB'],self.tab('MongoDB'))
    self.mongodb.grid(column=0,row=0,padx=5,pady=5,sticky='ew')
    self.nodejs = NodeJS(PPIM['NodeJS'],self.tab('NodeJS'))
    self.nodejs.grid(column=0,row=0,padx=5,pady=5,sticky='ew')
    self.payload = Payload(PPIM['Payload'],self.tab('Payload'))
    self.payload.grid(column=0,row=0,padx=5,pady=5,sticky='ew')
    self.ui = UI(PPIM['UI'],self.tab('UI'))
    self.ui.grid(column=0,row=0,padx=5,pady=5,sticky='ew')
    self.updates = Updates(PPIM['Updates'],self.tab('Updates'))
    self.updates.grid(column=0,row=0,padx=5,pady=5,sticky='ew')

