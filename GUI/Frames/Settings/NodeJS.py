import customtkinter as ctk
from GUI.Frames.Reusable.ArrayFrame import ArrayFrame

class NodeJS(ctk.CTkFrame):
  def __init__(self,current,*args,**kwargs):
    super().__init__(
      fg_color='transparent',
      bg_color='transparent',
      *args,**kwargs)
    self.columnconfigure(0,weight=1)
    self.columnconfigure(1,weight=0)
    self.columnconfigure(2,weight=0)
    scriptcommands = ['NPM','Yarn']
    self.form= {
      'labels':{
        'ScriptCommand':ctk.CTkLabel(self,text='Script Command:',anchor='w'),
        'Dependencies':ctk.CTkLabel(self,text='Default Dependencies:',anchor='w'),
        'Dev-Dependencies':ctk.CTkLabel(self,text='Default Dev Dependencies:',anchor='w'),
      },
      'inputs':{
        'ScriptCommand':ctk.CTkOptionMenu(self,values=scriptcommands),
        'Dependencies':ArrayFrame(self),
        'Dev-Dependencies':ArrayFrame(self)
      },
    }

    self.devadd:ArrayFrame = self.form['inputs']['Dev-Dependencies']
    self.depadd:ArrayFrame = self.form['inputs']['Dependencies']

    self.addDep = ctk.CTkButton(self,text='+',corner_radius=14,width=0,command=self.depadd.AddDependency)
    self.addDep.grid(column=2,row=1,padx=5,pady=5,sticky='ew')
    
    self.addDev = ctk.CTkButton(self,text='+',corner_radius=14,width=0,command=self.devadd.AddDependency)
    self.addDev.grid(column=2,row=3,padx=5,pady=5,sticky='ew')

    row = 0
    column = 0
    for group, fields in self.form.items():
      fields:dict
      for field in fields:
        f:ctk.CTkBaseClass = self.form[group][field]
        if group == 'labels':
          f.grid(column=column,row=row,padx=5,pady=5,sticky='ew')
          if field == 'ScriptCommand':
            row += 1
          if field == 'Dependencies':
            row += 2
        if group == 'inputs':
          if field == 'ScriptCommand':
            row = 0
            column = 1
            f.grid(column=column,row=row,columnspan=2,padx=5,pady=5,sticky='ew')
            row += 2
          else:
            column=0
            f.grid(column=column,columnspan=3,row=row,padx=5,pady=5,sticky='ew')
            row+=2

    