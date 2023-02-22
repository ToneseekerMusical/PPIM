import customtkinter as ctk
from GUI.Frames.Settings.settings import SettingsGroups
from GUI.Frames.Settings.Frames.ArrayFrame import ArrayFrame
from pymongo.database import Database

class AppSettings(ctk.CTkToplevel):
  def __init__(self, windowName:str, PPIM:Database, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.windowName = windowName
    self.PPIM = PPIM
    self.grab_set()
    self.focus_force()
    self.wm_title(f'{self.windowName.replace("-"," ")} Settings')
    self.transient()
    self.resizable(False,False)
    self.update()
    self.grid_columnconfigure(0,minsize=350,weight=1)
    self.settings = SettingsGroups(self.PPIM,self)
    self.settings.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
    self.save = ctk.CTkButton(self,text='Save',command=self.save)
    self.save.grid(row=1,column=1,padx=10,pady=(0,10))

    sh = self.winfo_screenheight()//2
    sw = self.winfo_screenwidth()//2
    self.geometry(f"{sw-250}+{sh-350}")

  def save(self):
    tab = self.settings._segmented_button.get()
    frame = self.settings.tab(tab).children[f'!{tab.lower()}']
    form = frame.__dict__['form']
    form:dict
    settings = {}
    if tab in ('Accounts','Directories'):
      settings[tab] = {}
      for setting, groups in form.items():
        settings[tab][setting] = {}
        groups:dict
        for group, fields in groups.items():
          if group == 'inputs':
            fields:dict
            for name, field in fields.items():
              if type(field) == ctk.CTkLabel:
                settings[tab][setting][name] = field.cget('text')
              else:
                settings[tab][setting][name] = field.get()
    else:
      dep = {}
      for group, fields in form.items():
        settings[tab] = {}
        if group == 'inputs':
          for name, field in fields.items():
            if type(field) == ctk.CTkLabel:
              settings[tab][name] = field.cget('text')
            elif type(field) == ArrayFrame:
              field:ArrayFrame
              for dependency, grps in field.form.items():
                for grp, flds in grps.items():
                  if grp == 'inputs':
                    dep[flds['Name'].get()] = flds['Version'].get()
                settings[tab][name] = dep
              dep = {}
            else:
              settings[tab][name] = field.get()
    self.PPIM.get_collection('Settings').update_one({'_id':'Settings'},update={"$set":settings},upsert=True)