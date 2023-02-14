import customtkinter as ctk
from Controllers.Mongo import MongoCompass
from Controllers.Mongo import MongoSH

class siteSetup(ctk.CTkTabview):
  def __init__(self, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      width=5,
      height=5,
      *args,
      **kwargs)
    #create shell frame
    self.add('Site Setup')
    self.collections = ctk.CTkButton(self.tab('Site Setup'),text='Collections')
    self.collections.grid(row=0,column=0,padx=5,pady=5,sticky='ew')
    self.userRoles = ctk.CTkButton(self.tab('Site Setup'),text='User Roles')
    self.userRoles.grid(row=1,column=0,padx=5,pady=5,sticky='ew')
    self.accessControl = ctk.CTkButton(self.tab('Site Setup'),text='Permissions')
    self.accessControl.grid(row=2,column=0,padx=5,pady=5,sticky='ew')
    self.accessControl = ctk.CTkButton(self.tab('Site Setup'),text='Custom componenets')
    self.accessControl.grid(row=3,column=0,padx=5,pady=5,sticky='ew')