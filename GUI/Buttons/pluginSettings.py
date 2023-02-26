import customtkinter as ctk
from GUI.Views import PluginSettings

class PluginSettingsBtn(ctk.CTkButton):
  def __init__(self,pluginName:str,*args,**kwargs):
    super().__init__(
      text=pluginName.replace('-',' '),
      *args,**kwargs)
    self.pluginName = pluginName
    self._command = self.Open
    

  def Open(self):
    self.win = PluginSettings(self.pluginName,self)

class PluginSettingsSwitch(ctk.CTkSwitch):
  def __init__(self,pluginName:str,*args,**kwargs):
    super().__init__(
      text=pluginName.replace('-',' '),
      *args,**kwargs)
    self.pluginName = pluginName
    self._command = self.setState
    self._onvalue = True
    self._offvalue = False
    

  def setState(self):
    if self.get() == False:
      self.master.master.inputs['Plugin Settings'][self.pluginName].configure(state='disabled')
    else:
      self.master.master.inputs['Plugin Settings'][self.pluginName].configure(state='normal')
