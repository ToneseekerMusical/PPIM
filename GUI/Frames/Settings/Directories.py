import customtkinter as ctk
from pathlib import Path
from GUI.Buttons import DirSelectBtn

class Directories(ctk.CTkFrame):
  def __init__(self,current,*args,**kwargs):
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
      self.form[setting]['labels'] = {}
      self.form[setting]['inputs'] = {}
      self.form[setting]['button'] = {}
      self.form[setting]['labels']['directory']=ctk.CTkLabel(self.form[setting]['frame'],text=f'{setting.replace("-"," ")}:', anchor='w')
      self.form[setting]['labels']['directory'].grid(column=0,row=0,sticky='ew')
      self.form[setting]['inputs']['directory']=ctk.CTkLabel(self.form[setting]['frame'],text='No Directory Set',anchor='w')
      self.form[setting]['inputs']['directory'].grid(column=0,row=1,columnspan=2,sticky='ew')
      self.form[setting]['button']['directory']=DirSelectBtn(setting.replace('-',' '),f'{Path.cwd()}\\lib',
              self.form[setting]['inputs']['directory'],self.form[setting]['frame'],text='Select Directory')
      self.form[setting]['button']['directory'].grid(column=1,row=0,sticky='ew')
      row += 1