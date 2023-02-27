import customtkinter as ctk
from GUI.Buttons.PluginSettings import PluginSettingsBtn
from GUI.Buttons.PluginSettings import PluginSettingsSwitch

class PluginFrame(ctk.CTkTabview):
  def __init__(self, plugins, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      width=5,
      height=5,
      *args,
      **kwargs)
    self.plugins = plugins
    self.tabs = ['Plugin Settings','Manage']
    self.add('Plugin Settings')
    self.add('Manage')
    self.tab('Plugin Settings').grid_columnconfigure((0,1), minsize=150, weight=1)
    self.tab('Manage').grid_columnconfigure((0,1), minsize=150, weight=1)
    self.inputs = {'Plugin Settings':{},'Manage':{}}

    row = 0
    column = 0
    rowIndeces = []
    for tab, groups in self.inputs.items():
      for plugin, settings in self.plugins.items():
        if tab == 'Plugin Settings':
          self.inputs[tab][plugin] = PluginSettingsBtn(plugin,self.tab(tab))
          self.inputs[tab][plugin].grid(row=row,column=column,padx=5,pady=5,sticky='ew')
          if settings['enabled'] == False:
            self.inputs[tab][plugin].configure(state='disabled')
        if tab == 'Manage':
          self.inputs[tab][plugin] = PluginSettingsSwitch(plugin,self.tab(tab))
          self.inputs[tab][plugin].grid(row=row,column=column,padx=5,pady=6.5,sticky='ew')
          if settings['enabled'] == True:
            self.inputs[tab][plugin].select()
        rowIndeces.append(row)
        column += 1
        if column >= len(self.plugins)//5:
          column = 0
          row += 1
      row = 0
      column = 0
    row = 0
    column = 0
    rowIndeces = [*set(rowIndeces)]
    self.tab('Plugin Settings').grid_rowconfigure(rowIndeces,weight=1)
    self.tab('Manage').grid_rowconfigure(rowIndeces,weight=1)
