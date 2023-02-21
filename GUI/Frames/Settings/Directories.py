import customtkinter as ctk
from pathlib import Path
from GUI.Buttons.dirSelect import dirSelect

class Directories(ctk.CTkFrame):
  def __init__(self,*args,**kwargs):
    super().__init__(
      bg_color='transparent',
      fg_color='transparent',
      *args,**kwargs)
    self.form = {
      'Project-Directory':{},
      'NodeJS-Directory':{},
      'VSCode-Directory':{},
      'MongoDB-Directory':{},
      'Mongosh-Directory':{},
      'Compass-Directory':{},
      'Github-Directory':{},
      'DBTools-Directory':{},
    }
    self.grid_columnconfigure(0, weight=1)
    row = 0
    for setting in self.form.keys():
      self.form[setting]['frame']=ctk.CTkFrame(self,bg_color='transparent',fg_color='transparent')
      self.form[setting]['frame'].grid(column = 0, pady=(0,10), row=row,sticky='ew')
      self.form[setting]['frame'].grid_columnconfigure(0,weight=1)
      self.form[setting]['label']=ctk.CTkLabel(self.form[setting]['frame'],text=f'{setting.replace("-"," ")}:', anchor='w')
      self.form[setting]['label'].grid(column=0,row=0,sticky='ew')
      self.form[setting]['value']=ctk.CTkLabel(self.form[setting]['frame'],text='No Directory Set',anchor='w')
      self.form[setting]['value'].grid(column=0,row=1,columnspan=2,sticky='ew')
      self.form[setting]['input']=dirSelect(setting.replace('-',' '),f'{Path.cwd()}\\lib',
              self.form[setting]['value'],self.form[setting]['frame'],text='Select Directory')
      self.form[setting]['input'].grid(column=1,row=0,sticky='ew')
      row += 1