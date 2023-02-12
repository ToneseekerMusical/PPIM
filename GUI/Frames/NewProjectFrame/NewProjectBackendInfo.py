import customtkinter as ctk

class BackendFrame(ctk.CTkTabview):
  def __init__(self, mongoVersions, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      width=5,
      height=5,
      *args,
      **kwargs
      )
    
    self.add('Backend Config')

    self.labels = {
      'mongoDBversion': ctk.CTkLabel(self.tab('Backend Config'),text='MongoDB Version:'),
      'databaseURI': ctk.CTkLabel(self.tab('Backend Config'),text='Database Url:'),
      'databaseName': ctk.CTkLabel(self.tab('Backend Config'),text='Database Name:'),
    }

    self.__rowcount = 0
    for label in self.labels:
      self.labels[label].grid(row = self.__rowcount,column=0,padx=5,pady=5,sticky='W')
      self.__rowcount += 1

    self.inputs = {
      'mongoDBVersion':ctk.CTkOptionMenu(self.tab('Backend Config'),values=mongoVersions),
      'databaseURI': ctk.CTkLabel(self.tab('Backend Config'),text='mongodb://localhost:27017',anchor='w'),
      'databaseName': ctk.CTkLabel(self.tab('Backend Config'),text='',anchor='w'),
      'editDBName': ctk.CTkSwitch(self.tab('Backend Config'),text='Edit Database',command=self.EditDBName)
    }

    self.__rowcount=0
    for field in self.inputs:
      self.inputs[field].grid(row=self.__rowcount,column=1,padx=5,pady=5,sticky='ew')
      self.__rowcount += 1

  def EditDBName(self):
    if not hasattr(self,'dbName'):
      self.dbName = self.inputs['databaseName'].cget('text')
      self.dbURI = self.inputs['databaseURI'].cget('text')
    if self.inputs['editDBName'].get() == 1:
      dbName = self.inputs['databaseName'].cget('text')
      dbURI = self.inputs['databaseURI'].cget('text')
      self.inputs['databaseName'].destroy()
      self.inputs['databaseURI'].destroy()
      self.inputs['databaseName'] = ctk.CTkEntry(self.tab('Backend Config'),placeholder_text=dbName)
      self.inputs['databaseURI'] = ctk.CTkEntry(self.tab('Backend Config'),placeholder_text=dbURI)
      self.inputs['databaseUsername'] = ctk.CTkEntry(self.tab('Backend Config'),placeholder_text='Username')
      self.inputs['databasePassword'] = ctk.CTkEntry(self.tab('Backend Config'),placeholder_text='Password',show="\u2022")
      self.inputs['databaseUsername'].grid(row=3,column=1,padx=5,pady=5,sticky='ew')
      self.inputs['databasePassword'].grid(row=4,column=1,padx=5,pady=5,sticky='ew')
      self.inputs['editDBName'].grid(row=5,column=1,padx=5,pady=5,sticky='ew')
    else:
      dbName = self.inputs['databaseName'].get()
      self.inputs['databaseName'].destroy()
      self.inputs['databaseURI'].destroy()
      self.inputs['databaseUsername'].destroy()
      self.inputs['databasePassword'].destroy()
      self.inputs['databaseName'] = ctk.CTkLabel(self.tab('Backend Config'),text=self.dbName, anchor='w')
      self.inputs['databaseURI'] = ctk.CTkLabel(self.tab('Backend Config'),text=self.dbURI, anchor='w')
      self.inputs['editDBName'].grid(row=3,column=1,padx=5,pady=5,sticky='ew')
    self.inputs['databaseURI'].grid(row=1,column=1,padx=5,pady=5,sticky='ew')
    self.inputs['databaseName'].grid(row=2,column=1,padx=5,pady=5,sticky='ew')
      

      #'databaseURI':ctk.CTkEntry(self.tab('Backend Config')),