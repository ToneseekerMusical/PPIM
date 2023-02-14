import customtkinter as ctk

class devTools(ctk.CTkTabview):
  def __init__(self, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      width=5,
      height=5,
      *args,
      **kwargs)
    #create shell frame
    self.add('Dev Tools')
    self.startFrontend = ctk.CTkButton(self.tab('Dev Tools'),text='Start Frontend')
    self.startFrontend.grid(row=0,column=0,padx=5,pady=5,sticky='ew')
    self.pushFrontend = ctk.CTkButton(self.tab('Dev Tools'),text='Push Frontend')
    self.pushFrontend.grid(row=1,column=0,padx=5,pady=5,sticky='ew')
    self.buildFrontend = ctk.CTkButton(self.tab('Dev Tools'),text='Build Frontend')
    self.buildFrontend.grid(row=2,column=0,padx=5,pady=5,sticky='ew')
    self.startAdmin = ctk.CTkButton(self.tab('Dev Tools'),text='Start Admin')
    self.startAdmin.grid(row=0,column=1,padx=5,pady=5,sticky='ew')
    self.pushAdmin = ctk.CTkButton(self.tab('Dev Tools'),text='Push Admin')
    self.pushAdmin.grid(row=1,column=1,padx=5,pady=5,sticky='ew')
    self.buildAdmin = ctk.CTkButton(self.tab('Dev Tools'),text='Build Admin')
    self.buildAdmin.grid(row=2,column=1,padx=5,pady=5,sticky='ew')