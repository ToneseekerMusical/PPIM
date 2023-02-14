import customtkinter as ctk
from Controllers.Mongo import MongoCompass
from Controllers.Mongo import MongoSH

class databaseInfo(ctk.CTkTabview):
  def __init__(self, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      width=5,
      height=5,
      *args,
      **kwargs)
    #create shell frame
    self.add('Database Info')
    self.add('Edit')

    self.tabs = {
      'databaseInfo':{
        'labels':{
          'databaseName':ctk.CTkLabel(self.tab('Database Info'),text='Database Name:',anchor='w'),
          'databaseHost':ctk.CTkLabel(self.tab('Database Info'),text='Database Host:',anchor='w'),
          'databasePort':ctk.CTkLabel(self.tab('Database Info'),text='Database Port:',anchor='w'),
          'databaseURI':ctk.CTkLabel(self.tab('Database Info'),text='Database URI:',anchor='w'),
        },
        'inputs':{
          'databaseName': ctk.CTkLabel(self.tab('Database Info'),text='Test',anchor='w'),
          'databaseHost': ctk.CTkLabel(self.tab('Database Info'),text='mongodb://localhost',anchor='w'),
          'databasePort': ctk.CTkLabel(self.tab('Database Info'),text='27017',anchor='w'),
          'databaseURI': ctk.CTkLabel(self.tab('Database Info'),text='mongodb://127.0.0.1:27017/',anchor='w'),
        }
      },
      'edit':{
        'labels':{
          'databaseName':ctk.CTkLabel(self.tab('Edit'),text='Database Name:',anchor='w'),
          'databaseHost':ctk.CTkLabel(self.tab('Edit'),text='Database Host:',anchor='w'),
          'databasePort':ctk.CTkLabel(self.tab('Edit'),text='Database Port:',anchor='w'),
          'databaseURI':ctk.CTkLabel(self.tab('Edit'),text='Database URI:',anchor='w'),
        },
        'inputs':{
          'databaseName':ctk.CTkEntry(self.tab('Edit'),placeholder_text='Test'),
          'databaseHost':ctk.CTkEntry(self.tab('Edit'),placeholder_text='mongodb://localhost'),
          'databasePort':ctk.CTkEntry(self.tab('Edit'),placeholder_text='27017'),
          'databaseURI':ctk.CTkLabel(self.tab('Edit'),text='mongodb://127.0.0.1:27017/',anchor='w'),
        }
      }}

    row = 0
    column = 0
    for tab, groups in self.tabs.items():
      for group, fields in groups.items():
        for field in fields.keys():
          self.tabs[tab][group][field].grid(row=row,column=column,padx=5,pady=5,sticky='ew')
          row += 1
        row = 0
        column += 1
      row = 0
      column = 0

    row = len(self.tabs['databaseInfo']['labels'])

    self.tabs['databaseInfo']['inputs']['compassbtn'] = ctk.CTkButton(self.tab('Database Info'),text='Open Compass',command=MongoCompass.startCompass)
    self.tabs['databaseInfo']['inputs']['compassbtn'].grid(column=0,row=row,padx=5,pady=5,sticky='ew')
    self.tabs['databaseInfo']['inputs']['mongoshbtn'] = ctk.CTkButton(self.tab('Database Info'),text='Open Mongosh',command=MongoSH.startMongosh)
    self.tabs['databaseInfo']['inputs']['mongoshbtn'].grid(column=1,row=row,padx=5,pady=5,sticky='ew')

    row = len(self.tabs['edit']['labels'])

    self.tabs['edit']['inputs']['userName'] = ctk.CTkEntry(self.tab('Edit'),placeholder_text='Username')
    self.tabs['edit']['inputs']['userName'].grid(row=row,column=0,padx=5,pady=5,sticky='ew')
    self.tabs['edit']['inputs']['passwords'] = ctk.CTkEntry(self.tab('Edit'),placeholder_text='Password',show="\u2022")
    self.tabs['edit']['inputs']['passwords'].grid(row=row,column=1,padx=5,pady=5,sticky='ew')