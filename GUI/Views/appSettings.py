import customtkinter as ctk
from GUI.Frames.appSettings import SettingsFrame

class AppSettings(ctk.CTkToplevel):
  def __init__(self, windowName:str, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.windowName = windowName
    self._current_height = 500
    #sh = self.winfo_screenheight()//2
    #sw = self.winfo_screenwidth()//2
    self.grab_set()
    self.focus_force()
    self.wm_title(f'{self.windowName.replace("-"," ")} Settings')
    self.transient()
    self.resizable(False,False)
    self.update()
    self.settings = SettingsFrame(self)
    self.settings.pack()

    #wh = self.winfo_height()//2
    #ww = self.winfo_width()//2
    #self.geometry(f"{sw-ww}+{sh-wh}")

    # create label on CTkToplevel window
    #label = ctk.CTkLabel(self, text=self.pluginName)
    #label.pack(side="top", fill="both", expand=True, padx=20, pady=20)