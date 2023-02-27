import customtkinter as ctk
from GUI.Frames.SettingsFrames.DirectoriesFrame import DirectoriesFrame
from GUI.Frames.SettingsFrames.AccountsFrame import AccountsFrame
from GUI.Frames.SettingsFrames.MongoDBFrame import MongoDBFrame
from GUI.Frames.SettingsFrames.NodeJSFrame import NodeJSFrame
from GUI.Frames.SettingsFrames.PayloadFrame import PayloadFrame
from GUI.Frames.SettingsFrames.UIFrame import UIFrame
from GUI.Frames.SettingsFrames.UpdatesFrame import UpdatesFrame

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

    self.accounts = AccountsFrame(PPIM['Accounts'],self.tab('Accounts'))
    self.accounts.grid(column=0,row=0,padx=5,pady=5)
    self.directories = DirectoriesFrame(PPIM['Directories'],self.tab('Directories'))
    self.directories.grid(column=0,row=0,padx=5,pady=5,sticky='ew')
    self.mongodb = MongoDBFrame(PPIM['MongoDB'],self.tab('MongoDB'))
    self.mongodb.grid(column=0,row=0,padx=5,pady=5,sticky='ew')
    self.nodejs = NodeJSFrame(PPIM['NodeJS'],self.tab('NodeJS'))
    self.nodejs.grid(column=0,row=0,padx=5,pady=5,sticky='ew')
    self.payload = PayloadFrame(PPIM['Payload'],self.tab('Payload'))
    self.payload.grid(column=0,row=0,padx=5,pady=5,sticky='ew')
    self.ui = UIFrame(PPIM['UI'],self.tab('UI'))
    self.ui.grid(column=0,row=0,padx=5,pady=5,sticky='ew')
    self.updates = UpdatesFrame(PPIM['Updates'],self.tab('Updates'))
    self.updates.grid(column=0,row=0,padx=5,pady=5,sticky='ew')

