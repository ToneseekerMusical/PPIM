import customtkinter as ctk
from GUI.Views.appSettings import AppSettings

class AppSettingsBtn(ctk.CTkButton):
  def __init__(self,windowName:str,*args,**kwargs):
    super().__init__(*args,**kwargs)

    self.windowName = windowName
    self._command=self.Open
    self.open=False
    self.win=None

  def Open(self):
    if self.open == False:
      self.win = AppSettings(self.windowName,self)
      self.win.protocol('WM_DELETE_WINDOW',self.openCheck)

      self.open=True
      self.configure(state='disabled')

  def openCheck(self):
    if self.open == True:
      self.open = False
      self.configure(state='normal')
      self.win.destroy()