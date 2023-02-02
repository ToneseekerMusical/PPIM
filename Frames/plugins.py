import customtkinter

class pluginFrame(customtkinter.CTkFrame):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
        #Plugin Select Frame

    self.pluginLabel = customtkinter.CTkLabel(
      self,
      text='Plugins'
    )
    self.pluginLabel.grid(
      row=0,
      column=0,
      pady=5,
      padx=10,
      sticky='w'
    )

    self.plugincloudstorage = customtkinter.CTkCheckBox(
      self,
      text='Cloud Storage'
    )
    self.plugincloudstorage.grid(
      row=1,
      column=0,
      pady=5,
      padx=10,
      sticky='w'
    )

    self.pluginseo = customtkinter.CTkCheckBox(
      self,
      text='SEO'
    )
    self.pluginseo.grid(
      row=1,
      column=1,
      pady=5,
      sticky='w'
    )

    self.pluginformbuilder = customtkinter.CTkCheckBox(
      self,
      text='Form Builder'
    )
    self.pluginformbuilder.grid(
      row=1,
      column=2,
      pady=5,
      sticky='w'
    )

    self.plugins3uload = customtkinter.CTkCheckBox(
      self,
      text='S3 Upload'
    )
    self.plugins3uload.grid(
      row=1,
      column=3,
      pady=5,
      sticky='w'
    )

    self.payloadpluginlexical = customtkinter.CTkCheckBox(
      self,
      text='Lexical'
    )
    self.payloadpluginlexical.grid(
      row=1,
      column=4,
      pady=5,
      sticky='w'
    )

    self.payloadpluginsearch = customtkinter.CTkCheckBox(
      self,
      text='Search'
    )
    self.payloadpluginsearch.grid(
      row=1,
      column=5,
      pady=5,
      sticky='w'
    )

    self.payloadwebp = customtkinter.CTkCheckBox(
      self,
      text='WebP'
    )
    self.payloadwebp.grid(
      row=2,
      column=0,
      pady=5,
      padx=10,
      sticky='w'
    )
    
    self.payloadblurhashplugin = customtkinter.CTkCheckBox(
      self,
      text='Blurhash'
    )
    self.payloadblurhashplugin.grid(
      row=2,
      column=1,
      pady=5,
      sticky='w'
    )    

    self.pluginstripe = customtkinter.CTkCheckBox(
      self,
      text='Stripe'
    )
    self.pluginstripe.grid(
      row=2,
      column=2,
      pady=5,
      sticky='w'
    )

    self.payloadauth0plugin = customtkinter.CTkCheckBox(
      self,
      text='Auth0'
    )
    self.payloadauth0plugin.grid(
      row=2,
      column=3,
      pady=5,
      sticky='w'
    )

    self.payloadcloudinaryplugin = customtkinter.CTkCheckBox(
      self,
      text='Cloudinary'
    )
    self.payloadcloudinaryplugin.grid(
      row=2,
      column=4,
      pady=5,
      sticky='w'
    )

    self.pluginnesteddocs = customtkinter.CTkCheckBox(
      self,
      text='NestedDocs'
    )
    self.pluginnesteddocs.grid(
      row=2,
      column=5,
      pady=5,
      sticky='w'
    )

    self.payloadhashupload = customtkinter.CTkCheckBox(
      self,
      text='Hash Upload'
    )
    self.payloadhashupload.grid(
      row=3,
      column=0,
      pady=5,
      padx=10,
      sticky='w'
    )

    self.payloadpluginoauth = customtkinter.CTkCheckBox(
      self,
      text='oAuth'
    )
    self.payloadpluginoauth.grid(
      row=3,
      column=1,
      pady=5,
      sticky='w'
    )

    self.payloadimagekit = customtkinter.CTkCheckBox(
      self,
      text='Image Kit'
    )
    self.payloadimagekit.grid(
      row=3,
      column=2,
      pady=5,
      sticky='w'
    )

    self.payloadrediscache = customtkinter.CTkCheckBox(
      self,
      text='Redis Cache'
    )
    self.payloadrediscache.grid(
      row=3,
      column=3,
      pady=5,
      sticky='w'
    )
    
    self.pluginzapier = customtkinter.CTkCheckBox(
      self,
      text='Zapier'
    )
    self.pluginzapier.grid(
      row=3,
      column=4,
      pady=5,
      sticky='w'
    )

    self.payloadplugingoogleonetap = customtkinter.CTkCheckBox(
      self,
      text='Google One Tap'
    )
    self.payloadplugingoogleonetap.grid(
      row=3,
      column=5,
      pady=5,
      sticky='w'
    )

    self.payloadpluginphonefield = customtkinter.CTkCheckBox(
      self,
      text='Phone Field'
    )
    self.payloadpluginphonefield.grid(
      row=4,
      column=0,
      pady=5,
      padx=10,
      sticky='w'
    )

    self.payloaddefaultroles = customtkinter.CTkCheckBox(
      self,
      text='Default Roles'
    )
    self.payloaddefaultroles.grid(
      row=4,
      column=1,
      pady=5,
      sticky='w'
    )
