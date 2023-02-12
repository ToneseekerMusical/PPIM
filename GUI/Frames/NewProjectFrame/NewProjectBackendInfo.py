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
      'databaseURI':ctk.CTkEntry(self.tab('Backend Config')),
      'databaseName': ctk.CTkLabel(self.tab('Backend Config'),text='',anchor='w'),
      'editDBName': ctk.CTkSwitch(self.tab('Backend Config'),text='Edit Database Name',command=self.EditDBName)
    }

    self.inputs['databaseURI'].insert("0",'mongodb://localhost:27017')

    self.__rowcount=0
    for field in self.inputs:
      self.inputs[field].grid(row=self.__rowcount,column=1,padx=5,pady=5,sticky='ew')
      self.__rowcount += 1

  def EditDBName(self):
    if not hasattr(self,'dbName'):
      self.dbName = self.inputs['databaseName'].cget('text')
    if self.inputs['editDBName'].get() == 1:
      dbName = self.inputs['databaseName'].cget('text')
      self.inputs['databaseName'].destroy()
      self.inputs['databaseName'] = ctk.CTkEntry(self.tab('Backend Config'),placeholder_text=dbName)
    else:
      dbName = self.inputs['databaseName'].get()
      self.inputs['databaseName'].destroy()
      self.inputs['databaseName'] = ctk.CTkLabel(self.tab('Backend Config'),text=self.dbName, anchor='w')
    self.inputs['databaseName'].grid(row=2,column=1,padx=5,pady=5,sticky='ew')
      