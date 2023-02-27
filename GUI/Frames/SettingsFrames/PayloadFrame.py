import customtkinter as ctk

class PayloadFrame(ctk.CTkFrame):
  def __init__(self,*args,templates:dict={},adminaccount={},plugins:dict={},current,**kwargs):
    super().__init__(bg_color='transparent',fg_color='transparent',*args,**kwargs)

    if templates == {}:
      self.templates = [
        'blank',
        'blog',
        'todo'
      ]
    else:
      self.templates = templates
    
    if adminaccount == {}:
      self.adminPassword = ''
      self.adminUsername = ''
    else:
      self.adminPassword = current['AdminPassword']
      self.adminUsername = current['AdminUsername']

    if plugins == {}:
      self.plugins = {'Auth0':{},'Blurhash':{},'Cloud-Storage':{},'Cloudinary':{},'Default-Roles':{},
      'Form-Builder':{},'Google-One-Tap':{},'Hash-Upload':{},'Image-Kit':{},'Lexical':{},'NestedDocs':{},
      'oAuth':{},'Phone-Field':{},'Redis-Cache':{},'S3-Upload':{},'Search':{},'SEO':{},'Stripe':{},'webP':{},
      'Zapier':{},'Redirects':{},'Base-64':{},'Password-Protection':{},'Resolve-Alias':{},'Tenancy':{}}
    else:
      self.plugins = plugins

    self.form = {
      'labels':{
        'defaultTemplate':ctk.CTkLabel(self,text='Default Template:',anchor='w'),
        'defaultAdminName':ctk.CTkLabel(self,text='Default Username:',anchor='w'),
        'defaultAdminPassword':ctk.CTkLabel(self,text='Default Password:',anchor='w'),
        'defaultPlugins': ctk.CTkLabel(self,text='Default Plugins:',anchor='w')
      },
      'inputs':{
        'defaultTemplate':ctk.CTkOptionMenu(self,values=self.templates),
        'defaultAdminName':ctk.CTkEntry(self,placeholder_text='Username'),
        'defaultAdminPassword':ctk.CTkEntry(self,placeholder_text='Password',show='\u2022')
      }
    }

    column = 0
    row = 0
    pluginstartrow = 0
    for name, group in self.form.items():
      group:dict
      for field in group.keys():
        if name == 'labels':
          self.form[name][field].grid(column=0,row=row,padx=5,pady=5,sticky='ew')
          row += 1
          pluginstartrow += 1
        if name == 'inputs':
          self.form[name][field].grid(column=1,columnspan=2,row=row,padx=5,pady=5,sticky='ew')
          if field == 'defaultAdminName':
            self.form[name][field].insert('0',self.adminUsername)
          if field == 'defaultAdminPassword':
            self.form[name][field].insert('0',self.adminPassword)
          row += 1
      row = 0
    row = pluginstartrow
    for name in self.plugins.keys():
      name:str
      self.form['inputs'][name] = ctk.CTkCheckBox(self,text=name.replace('-','-'),onvalue=True,offvalue=False)
      self.form['inputs'][name].grid(row=row,column=column,padx=5,pady=5,sticky='ew')
      column += 1
      if column >= 3:
        row += 1
        column  = 0


