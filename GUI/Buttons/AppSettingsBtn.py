import customtkinter as ctk
from GUI.Views import AppSettings
from Controllers.Mongo import MongoDB

class AppSettingsBtn(ctk.CTkButton):
  def __init__(self,windowName:str,PPIM:MongoDB,*args,**kwargs):
    super().__init__(*args,**kwargs)

    self.windowName = windowName
    self._command=self.Open
    self.open=False
    self.win=None
    self.PPIM = PPIM

  def Open(self):
    if self.open == False:
      self.win = AppSettings(self.windowName,self.PPIM,self)
      self.win.protocol('WM_DELETE_WINDOW',self.openCheck)

      self.open=True
      self.configure(state='disabled')

  def openCheck(self):
    if self.open == True:
      self.open = False
      self.configure(state='normal')
      self.win.destroy()