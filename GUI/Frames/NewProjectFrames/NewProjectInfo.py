import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path

class ProjectFrame(ctk.CTkTabview):
  def __init__(self, dbinfo, github, gitUser, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      width=150,
      height=5,
      segmented_button_selected_color=('#979DA2', 'gray29'),
      segmented_button_selected_hover_color=('#979DA2', 'gray29'),
      *args,
      **kwargs
      )
    
    self.dbinfo = dbinfo
    self.gitURL = f'https://github.com/{gitUser}'
    self.github = github

    self.add('Project Info')
    self.tab('Project Info').grid_columnconfigure((0,1), weight=1)

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
    if e.keysym != 'Tab':
      if e.keysym != 'BackSpace':
        self.inputs['dirPath'].configure(text=f'/websites/{self.inputs["siteName"].get()}{e.char}')
        self.dbinfo.tabs['backendConfig']['inputs']['databaseName'].configure(text=f'{self.inputs["siteName"].get()}{e.char}'.replace(' ','-'))
        self.dbinfo.tabs['backendConfig']['inputs']['databaseURI'].configure(text=f'mongodb://localhost:27017/{self.inputs["siteName"].get()}{e.char}'.replace(' ','-'))
        self.github.inputs['repoName'].configure(text=f'{self.inputs["siteName"].get()}{e.char}'.replace(' ','-'))
        self.github.inputs['repoURL'].configure(text=f'{self.gitURL}/{self.inputs["siteName"].get()}{e.char}'.replace(' ','-'))
      else:
        self.inputs['dirPath'].configure(text=f'/websites/{self.inputs["siteName"].get()[:-1]}')
        self.dbinfo.tabs['backendConfig']['inputs']['databaseName'].configure(text=f'{self.inputs["siteName"].get()[:-1]}'.replace(' ','-'))
        self.dbinfo.tabs['backendConfig']['inputs']['databaseURI'].configure(text=f'mongodb://localhost:27017/{self.inputs["siteName"].get()[:-1]}'.replace(' ','-'))
        self.github.inputs['repoName'].configure(text=f'{self.inputs["siteName"].get()[:-1]}'.replace(' ','-'))
        self.github.inputs['repoURL'].configure(text=f'{self.gitURL}/{self.inputs["siteName"].get()[:-1]}'.replace(' ','-'))
  
  def enableDirSelect(self,e):
    self.inputs['dirSelect'].configure(state='normal')
    self.inputs['siteName'].unbind('<key>')

