import customtkinter as ctk
from Controllers.Mongo import MongoCompass
from Controllers.Mongo import MongoSH

class databaseInfo(ctk.CTkTabview):
  def __init__(self, dbInfo, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      segmented_button_selected_color=('#979DA2', 'gray29'),
      segmented_button_selected_hover_color=('#979DA2', 'gray29'),
      width=5,
      height=5,
      *args,
      **kwargs)

    self.dbInfo = dbInfo

    self.add('Database Info')

    self.tabs = {
      'databaseInfo':{
        'labels':{
          'databaseName':ctk.CTkLabel(self.tab('Database Info'),text='Database Name:',anchor='w'),
          'databaseHost':ctk.CTkLabel(self.tab('Database Info'),text='Database Host:',anchor='w'),
          'databasePort':ctk.CTkLabel(self.tab('Database Info'),text='Database Port:',anchor='w'),
          'databaseURI':ctk.CTkLabel(self.tab('Database Info'),text='Database URI:',anchor='w'),
        },
        'inputs':{
          'databaseName': ctk.CTkLabel(self.tab('Database Info'),text=self.dbInfo['databaseName'],anchor='w'),
          'databaseHost': ctk.CTkLabel(self.tab('Database Info'),text=self.dbInfo['databaseHost'],anchor='w'),
          'databasePort': ctk.CTkLabel(self.tab('Database Info'),text=self.dbInfo['databasePort'],anchor='w'),
          'databaseURI': ctk.CTkLabel(self.tab('Database Info'),text=self.dbInfo['databaseURI'],anchor='w'),
          'openCompass':ctk.CTkButton(self.tab('Database Info'),text='Open Compass',command=lambda: MongoCompass.startCompass(self.dbInfo['databaseURI'])),
          'openMongosh':ctk.CTkButton(self.tab('Database Info'),text='Open Mongosh',command=lambda: MongoSH.startMongosh(self.dbInfo['databaseURI']))
          }
        },
      }

    row = 0
    column = 0
    labelrows=0
    for tab, groups in self.tabs.items():
      for group, fields in groups.items():
        for field in fields.keys():
          if group == 'labels':
            labelrows += 1
          self.tabs[tab][group][field].grid(row=row,column=column,padx=5,pady=5,sticky='ew')
          if row >= labelrows and column == 1:
            column = 0
            row -= 1
          elif row >= labelrows and column == 0:
            column += 1
          row += 1
        row = 0
        column += 1
      row = 0
      column = 0
      labelrows = 0