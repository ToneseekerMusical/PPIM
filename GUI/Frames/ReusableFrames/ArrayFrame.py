import customtkinter as ctk

class ArrayFrame(ctk.CTkScrollableFrame):
  def __init__(self,master,**kwargs):
    super().__init__(master,**kwargs)
    self.row=0
    self.form = {}
    self.row = 0
    self.depcount = 1
    self.grid_columnconfigure((0,1),weight=1)
  
  def AddDependency(self):
    self.form[f'Dependency{self.depcount}'] = {
      'labels':{
        'Name':ctk.CTkLabel(self,text='Name',anchor='w'),
        'Version':ctk.CTkLabel(self,text='Version',anchor='w'),
      },
      'inputs':{
        'Name':ctk.CTkEntry(self,placeholder_text='Dependency Name'),
        'Version':ctk.CTkEntry(self,placeholder_text='Dependency Version')
      }
    }
    column = 0
    for dependency, dependencies in self.form.items():
      dependencies:dict
      for group, groups in dependencies.items():
        groups:dict
        for field in groups.keys():
          field:ctk.CTkBaseClass = self.form[dependency][group][field]
          if not field.grid_info():
            field.grid(row=self.row,column=column,padx=5,pady=5,sticky='ew')
          if column == 0:
            column += 1
          else:
            column -= 1
        self.row += 1
    self.depcount +=1