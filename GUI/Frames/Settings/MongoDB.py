import customtkinter as ctk

class MongoDB(ctk.CTkFrame):
  def __init__(self,current,*args,**kwargs):
    super().__init__(fg_color='transparent',bg_color='transparent',*args,**kwargs)
    
    self.grid_columnconfigure((0,1),weight=1)

    self.form = {
      'labels':{
        'Username':ctk.CTkLabel(self,text='Username:',anchor='w'),
        'Password':ctk.CTkLabel(self,text='Password:',anchor='w'),
        'DefaultHost':ctk.CTkLabel(self,text='Default Host:',anchor='w'),
        'DefaultPort':ctk.CTkLabel(self,text='Default Port:',anchor='w'),
      },
      'inputs':{
        'Username':ctk.CTkEntry(self,placeholder_text='Username'),
        'Password':ctk.CTkEntry(self,placeholder_text='Password',show='\u2022'),
        'DefaultHost':ctk.CTkEntry(self,placeholder_text='localhost'),
        'DefaultPort':ctk.CTkEntry(self,placeholder_text='27017'),
      }
    }

    row=0
    column = 0
    for group, fields in self.form.items():
      fields:dict
      for field in fields.keys():
        f:ctk.CTkBaseClass = self.form[group][field]
        f.grid(column=column,row=row,padx=5,pady=5,sticky='ew')
        row += 1
      column += 1
      row = 0