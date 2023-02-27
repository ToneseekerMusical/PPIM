import customtkinter as ctk

class EditSiteFrame(ctk.CTkTabview):
  def __init__(self, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      width=5,
      height=5,
      segmented_button_selected_color=('#979DA2', 'gray29'),
      segmented_button_selected_hover_color=('#979DA2', 'gray29'),
      *args,
      **kwargs)
    #create shell frame
    self.add('Site Config')
    self.tab('Site Config').grid_columnconfigure((0,1),weight=1)
    self.collections = ctk.CTkButton(self.tab('Site Config'),text='Collections')
    self.collections.grid(row=0,column=0,padx=5,pady=5,sticky='ew')
    self.userRoles = ctk.CTkButton(self.tab('Site Config'),text='User Roles')
    self.userRoles.grid(row=0,column=1,padx=5,pady=5,sticky='ew')
    self.accessControl = ctk.CTkButton(self.tab('Site Config'),text='Permissions')
    self.accessControl.grid(row=1,column=0,padx=5,pady=5,sticky='ew')
    self.accessControl = ctk.CTkButton(self.tab('Site Config'),text='Custom Componenets')
    self.accessControl.grid(row=1,column=1,padx=5,pady=5,sticky='ew')
    self.accessControl = ctk.CTkButton(self.tab('Site Config'),text='White Label')
    self.accessControl.grid(row=2,column=0,padx=5,pady=5,sticky='ew')
    self.accessControl = ctk.CTkButton(self.tab('Site Config'),text='Update Payload')
    self.accessControl.grid(row=2,column=1,padx=5,pady=5,sticky='ew')