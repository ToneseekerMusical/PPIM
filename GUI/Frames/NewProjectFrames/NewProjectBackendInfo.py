import customtkinter as ctk

class BackendFrame(ctk.CTkTabview):
  def __init__(self, mongoVersions, *args, **kwargs):
    super().__init__(corner_radius=10,width=5,height=5,*args,**kwargs)
    
    self.add('Backend Config')
    self.add('Edit')
    self.tab('Backend Config').grid_columnconfigure((0,1),weight=0)
    self.tab('Edit').grid_columnconfigure((0,1),weight=1)

    self.configure(command=self.compileURI)

    self.tabs = {
      'backendConfig': {
        'labels': {
          'databaseVers': ctk.CTkLabel(self.tab('Backend Config'),text='MongoDB Version:',anchor='w'),
          'databaseHost': ctk.CTkLabel(self.tab('Backend Config'),text='Database Host:',anchor='w'),
          'databaseName': ctk.CTkLabel(self.tab('Backend Config'),text='Database Name:',anchor='w'),
          'databasePort': ctk.CTkLabel(self.tab('Backend Config'),text='Database Port:',anchor='w'),
          'databaseURI': ctk.CTkLabel(self.tab('Backend Config'),text='Database URI:',anchor='w'),
        },
        'inputs': {
          'databaseVers': ctk.CTkLabel(self.tab('Backend Config'),text='6.0.4',anchor='w'),
          'databaseHost': ctk.CTkLabel(self.tab('Backend Config'),text='localhost',anchor='w'),
          'databaseName': ctk.CTkLabel(self.tab('Backend Config'),text='',anchor='w'),
          'databasePort': ctk.CTkLabel(self.tab('Backend Config'),text='27017',anchor='w'),
          'databaseURI': ctk.CTkLabel(self.tab('Backend Config'),text='mongodb://localhost:27017',anchor='w'),
        }
      },
      'Edit': {
        'labels': {
          'databaseVers': ctk.CTkLabel(self.tab('Edit'),text='MongoDB Version:',anchor='w'),
          'databaseHost': ctk.CTkLabel(self.tab('Edit'),text='Database Host:',anchor='w'),
          'databaseName': ctk.CTkLabel(self.tab('Edit'),text='Database Name:',anchor='w'),
          'databasePort': ctk.CTkLabel(self.tab('Edit'),text='Database Port:',anchor='w'),
        },
        'inputs': {
          'databaseVers':ctk.CTkOptionMenu(self.tab('Edit'),values=mongoVersions,command=self.SetVersion),
          'databaseHost': ctk.CTkEntry(self.tab('Edit'),placeholder_text='localhost'),
          'databaseName': ctk.CTkEntry(self.tab('Edit'),placeholder_text=''),
          'databasePort': ctk.CTkEntry(self.tab('Edit'),placeholder_text='27017'),
          'username': ctk.CTkEntry(self.tab('Edit'),placeholder_text='Username'),
          'password': ctk.CTkEntry(self.tab('Edit'),placeholder_text='Password',show="\u2022")
        }
      }
    }

    self.tabs['Edit']['inputs']['databaseHost'].bind("<Key>",lambda event: self.labeller(event,'databaseHost'))
    self.tabs['Edit']['inputs']['databaseName'].bind("<Key>",lambda event: self.labeller(event,'databaseName'))
    self.tabs['Edit']['inputs']['databasePort'].bind("<Key>",lambda event: self.labeller(event,'databasePort'))

    row = 0
    column = 0

    for tab, groups in self.tabs.items():
      for group, fields in groups.items():
        for field in fields.keys():
          padx=5
          if tab == 'backendConfig' and group == 'labels':
            padx = 5
          self.tabs[tab][group][field].grid(row=row,column=column,padx=padx,pady=5,sticky='ew')
          row += 1
          if tab == 'Edit':
            if field == 'databasePort':
              column = 0
            if field == 'username':
              row -= 1
              column = 1
        row = 0
        column += 1
      column = 0
      row = 0

  def SetVersion(self,value):
    self.tabs['backendConfig']['inputs']['databaseVers'].configure(text=value)

  def labeller(self,e,name):
    if e.keysym != 'Tab':
      newtext = self.tabs["Edit"]["inputs"][name].get()
      if newtext == '':
        if not hasattr(self,f'first{name}'):
          setattr(self,f'first{name}',self.tabs['backendConfig']['inputs'][name].cget('text'))
        self.tabs['backendConfig']['inputs'][name].configure(text=getattr(self,f'first{name}'))
      elif e.keysym != 'BackSpace':
        self.tabs['backendConfig']['inputs'][name].configure(text=f'{newtext}{e.char}')
      else:
        self.tabs['backendConfig']['inputs'][name].configure(text=f'{newtext[:-1]}')
  
  def compileURI(self):
    name = self.tabs['backendConfig']['inputs']['databaseName'].cget('text')
    host = self.tabs['backendConfig']['inputs']['databaseHost'].cget('text')
    port = self.tabs['backendConfig']['inputs']['databasePort'].cget('text')
    user = self.tabs['Edit']['inputs']['username'].get()
    pwrd = self.tabs['Edit']['inputs']['password'].get()
    if user != '' and pwrd != '':
      auth=f'{user}:{pwrd}@'
    else:
      auth = ''
    self.tabs['backendConfig']['inputs']['databaseURI'].configure(text=f'mongodb://{auth}{host}:{port}/{name}')