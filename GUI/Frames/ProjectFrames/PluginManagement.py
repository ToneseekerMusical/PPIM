import customtkinter as ctk
from GUI.Buttons.pluginSettings import PluginSettingsBtn

class pluginManager(ctk.CTkTabview):
  def __init__(self, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      width=5,
      height=5,
      *args,
      **kwargs)
    self.plugins = {'Cloud-Storage':{'enabled':True},'SEO':{'enabled':True},'Form-Builder':{'enabled':True},'S3-Upload':{'enabled':True},
      'Lexical':{'enabled':True},'Search':{'enabled':True},'webP':{'enabled':True},'Blurhash':{'enabled':True},'Stripe':{'enabled':True},'Auth0':{'enabled':True},
      'Cloudinary':{'enabled':True},'NestedDocs':{'enabled':False},'Hash-Upload':{'enabled':True},'oAuth':{'enabled':True},'Image-Kit':{'enabled':True},
      'Redis-Cache':{'enabled':True},'Zapier':{'enabled':True},'Google-One-Tap':{'enabled':True},'Phone-Field':{'enabled':True},
      'Default-Roles':{'enabled':True}
    }
    self.tabs = ['Plugins','Manage']
    self.add('Plugins')
    self.add('Manage')
    self.inputs = {'Plugins':{'buttons':{}},'Manage':{'switches':{}}}

    row = 0
    column = 0
    for tab, groups in self.inputs.items():
      for group, groups in groups.items():
        for plugin, settings in self.plugins.items():
          if group == 'buttons':
            self.inputs[tab][group][plugin] = PluginSettingsBtn(plugin,self.tab(tab))
            self.inputs[tab][group][plugin].grid(row=row,column=column,padx=5,pady=5,sticky='ew')
          if group == 'switches':
            self.inputs[tab][group][plugin] = ctk.CTkSwitch(self.tab(tab),text=plugin.replace('-',' '))
            self.inputs[tab][group][plugin].grid(row=row,column=column,padx=11.5,pady=6.5,sticky='ew')
            if settings['enabled'] == True:
              self.inputs[tab][group][plugin].select()
          row += 1
          if row >= len(self.plugins)//2:
            row = 0
            column += 1
        row = 0 
      row = 0
      column = 0