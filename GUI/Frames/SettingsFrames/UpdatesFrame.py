import customtkinter as ctk

class UpdatesFrame(ctk.CTkFrame):
  def __init__(self,*args,current,**kwargs):
    super().__init__(bg_color='transparent',fg_color='transparent',*args,**kwargs)
    self.grid_columnconfigure((0,1),weight=1)
    frequency = ['On Startup','Once Per Day', 'Once Per Week']
    self.form = {
      'labels':{
        'checkFrequency':ctk.CTkLabel(self,text='Check Frequency:',anchor='w'),
        'reminderFrequency':ctk.CTkLabel(self,text='Reminder Frequency:',anchor='w'),
        'bandwidthLimit':ctk.CTkLabel(self,text='Bandwidth Limit (KB/s):',anchor='w'),
      },
      'inputs':{
        'checkFrequency':ctk.CTkOptionMenu(self,values=frequency),
        'reminderFrequency':ctk.CTkOptionMenu(self,values=frequency),
        'bandwidthLimit':ctk.CTkEntry(self,placeholder_text='No Limit')
      }
    }
    column = 0
    row = 0
    for group, fields in self.form.items():
      fields:dict
      for field in fields.keys():
        self.form[group][field].grid(column=column,row=row,padx=5,pady=5,sticky='ew')
        row += 1
      row = 0
      column += 1