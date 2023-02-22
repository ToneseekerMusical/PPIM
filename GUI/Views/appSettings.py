import customtkinter as ctk
from GUI.Frames.Settings.settings import SettingsGroups

class AppSettings(ctk.CTkToplevel):
  def __init__(self, windowName:str, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.windowName = windowName
    self.grab_set()
    self.focus_force()
    self.wm_title(f'{self.windowName.replace("-"," ")} Settings')
    self.transient()
    self.resizable(False,False)
    self.update()
    self.grid_columnconfigure(0,minsize=350,weight=1)
    self.settings = SettingsGroups(self)
    self.settings.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
    self.save = ctk.CTkButton(self,text='Save',command=self.save)
    self.save.grid(row=1,column=1,padx=10,pady=(0,10))

    sh = self.winfo_screenheight()//2
    sw = self.winfo_screenwidth()//2
    wh = self.winfo_height()//2
    ww = self.winfo_width()//2
    self.geometry(f"{sw-250}+{sh-350}")

    # create label on CTkToplevel window
    #label = ctk.CTkLabel(self, text=self.pluginName)
    #label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
  def save():...