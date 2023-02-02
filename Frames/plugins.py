import customtkinter

class pluginFrame(customtkinter.CTk):
  def __init__(self, tab):
    super().__init__()
        #Plugin Select Frame
    self.plugin_frame = customtkinter.CTkFrame(
      tab,
      corner_radius=0,
    )
    self.plugin_frame.grid(
      row=1,
      column=0,
      columnspan=2,
      sticky='new',
    )
    self.plugin_frame.grid_columnconfigure((0,1,2,3,4,5), weight=1)

    self.pluginLabel = customtkinter.CTkLabel(
      self.plugin_frame,
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
      self.plugin_frame,
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
      self.plugin_frame,
      text='SEO'
    )
    self.pluginseo.grid(
      row=1,
      column=1,
      pady=5,
      sticky='w'
    )

    self.pluginformbuilder = customtkinter.CTkCheckBox(
      self.plugin_frame,
      text='Form Builder'
    )
    self.pluginformbuilder.grid(
      row=1,
      column=2,
      pady=5,
      sticky='w'
    )

    self.plugins3uload = customtkinter.CTkCheckBox(
      self.plugin_frame,
      text='S3 Upload'
    )
    self.plugins3uload.grid(
      row=1,
      column=3,
      pady=5,
      sticky='w'
    )

    self.payloadpluginlexical = customtkinter.CTkCheckBox(
      self.plugin_frame,
      text='Lexical'
    )
    self.payloadpluginlexical.grid(
      row=1,
      column=4,
      pady=5,
      sticky='w'
    )

    self.payloadpluginsearch = customtkinter.CTkCheckBox(
      self.plugin_frame,
      text='Search'
    )
    self.payloadpluginsearch.grid(
      row=1,
      column=5,
      pady=5,
      sticky='w'
    )

    self.payloadwebp = customtkinter.CTkCheckBox(
      self.plugin_frame,
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
      self.plugin_frame,
      text='Blurhash'
    )
    self.payloadblurhashplugin.grid(
      row=2,
      column=1,
      pady=5,
      sticky='w'
    )    

    self.pluginstripe = customtkinter.CTkCheckBox(
      self.plugin_frame,
      text='Stripe'
    )
    self.pluginstripe.grid(
      row=2,
      column=2,
      pady=5,
      sticky='w'
    )

    self.payloadauth0plugin = customtkinter.CTkCheckBox(
      self.plugin_frame,
      text='Auth0'
    )
    self.payloadauth0plugin.grid(
      row=2,
      column=3,
      pady=5,
      sticky='w'
    )

    self.payloadcloudinaryplugin = customtkinter.CTkCheckBox(
      self.plugin_frame,
      text='Cloudinary'
    )
    self.payloadcloudinaryplugin.grid(
      row=2,
      column=4,
      pady=5,
      sticky='w'
    )

    self.pluginnesteddocs = customtkinter.CTkCheckBox(
      self.plugin_frame,
      text='NestedDocs'
    )
    self.pluginnesteddocs.grid(
      row=2,
      column=5,
      pady=5,
      sticky='w'
    )

    self.payloadhashupload = customtkinter.CTkCheckBox(
      self.plugin_frame,
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
      self.plugin_frame,
      text='oAuth'
    )
    self.payloadpluginoauth.grid(
      row=3,
      column=1,
      pady=5,
      sticky='w'
    )

    self.payloadimagekit = customtkinter.CTkCheckBox(
      self.plugin_frame,
      text='Image Kit'
    )
    self.payloadimagekit.grid(
      row=3,
      column=2,
      pady=5,
      sticky='w'
    )

    self.payloadrediscache = customtkinter.CTkCheckBox(
      self.plugin_frame,
      text='Redis Cache'
    )
    self.payloadrediscache.grid(
      row=3,
      column=3,
      pady=5,
      sticky='w'
    )
    
    self.pluginzapier = customtkinter.CTkCheckBox(
      self.plugin_frame,
      text='Zapier'
    )
    self.pluginzapier.grid(
      row=3,
      column=4,
      pady=5,
      sticky='w'
    )

    self.payloadplugingoogleonetap = customtkinter.CTkCheckBox(
      self.plugin_frame,
      text='Google One Tap'
    )
    self.payloadplugingoogleonetap.grid(
      row=3,
      column=5,
      pady=5,
      sticky='w'
    )

    self.payloadpluginphonefield = customtkinter.CTkCheckBox(
      self.plugin_frame,
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
      self.plugin_frame,
      text='Default Roles'
    )
    self.payloaddefaultroles.grid(
      row=4,
      column=1,
      pady=5,
      sticky='w'
    )
