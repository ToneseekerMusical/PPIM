import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path

class projectFrame(ctk.CTkTabview):
  def __init__(self, dbinfo, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      width=5,
      height=5,
      *args,
      **kwargs
      )
    self.dbinfo = dbinfo
    self.add('Project Info')

    self.inputs = {
      'siteName':ctk.CTkEntry(self.tab('Project Info'),placeholder_text='Project Name'),
      'userName':ctk.CTkEntry(self.tab('Project Info'),placeholder_text='User Name'),
      'password':ctk.CTkEntry(self.tab('Project Info'),placeholder_text='Password',show="\u2022"),
      'dirPath':ctk.CTkLabel(self.tab('Project Info'),text='\websites\...',anchor='w'),
      'dirSelect':ctk.CTkButton(self.tab('Project Info'),text='Choose Folder',
                                command=self.SelectDirectory),
    }
    
    self.inputs['dirSelect'].configure(state='disabled')
    self.inputs['siteName'].bind("<Key>",self.labeller)
    self.inputs['siteName'].bind("<Key>",self.enableDirSelect)

    name:str
    field:ctk.CTkBaseClass
    self.row = 0
    self.column = 0
    
    for name, field, in self.inputs.items():
      field.grid(row=self.row,column=self.column,padx=5,pady=5,sticky='ew')
      if name in ('siteName','dirPath'):
        field.grid(columnspan=2)
      if name in ('userName','dirPath'):
        self.column += 1
      else:
        self.row += 1
        self.column = 0

  def SelectDirectory(self):
    cwd = f'{Path().cwd()}'
    sitePath = Path(f'{cwd}\websites')
    sitePath = filedialog.askdirectory(initialdir=f'{sitePath}',
      title='Select PayloadCMS Instance Directory')
    if 'PPIM' in sitePath:
      sitePath = sitePath.split('PPIM')
    self.inputs['dirPath'].configure(text=sitePath[1])

  def labeller(self,e):
    self.inputs['dirPath'].configure(text=f'/websites/{self.inputs["siteName"].get()}{e.char}')
    self.dbinfo.inputs['databaseName'].configure(text=f'{self.inputs["siteName"].get()}{e.char}'.replace(' ','-'))
  def enableDirSelect(self,e):
    self.inputs['dirSelect'].configure(state='normal')
    self.inputs['siteName'].unbind('<key>')

