import customtkinter as ctk
from GUI.Frames.Settings.settings import SettingsGroups

class SettingsFrame(ctk.CTkFrame):
  def __init__(self,*args,**kwargs):
    super().__init__(
      bg_color='transparent',
      fg_color='transparent',
      *args,**kwargs)

    self.grid_columnconfigure(0,weight=1)
    self.settings = SettingsGroups(self)
    self.settings.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
    self.save = ctk.CTkButton(self,text='Save',command=self.save)
    self.save.grid(row=1,column=1,padx=10,pady=(0,10))

  def save():...