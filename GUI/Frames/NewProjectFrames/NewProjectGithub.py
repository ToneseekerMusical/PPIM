import customtkinter as ctk



class githubFrame(ctk.CTkTabview):
  def __init__(self, gitUser, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      width=5,
      height=5,
      segmented_button_selected_color=('#979DA2', 'gray29'),
      segmented_button_selected_hover_color=('#979DA2', 'gray29'),
      *args,
      **kwargs
      )
    
    self.gitURL = f'https://github.com/{gitUser}'

    self.add('Github Info')

    self.tab('Github Info').columnconfigure((0,1), weight=1)

    self.inputs = {
      'repoName': ctk.CTkLabel(self.tab('Github Info'),text='Repository Name',anchor='w'),
      'editName': ctk.CTkSwitch(self.tab('Github Info'),text='Edit Repo Name', onvalue=True,offvalue=False,command=self.renameRepo),
      'repoURL': ctk.CTkLabel(self.tab('Github Info'),anchor='w',text=self.gitURL),
      'cloneURL': ctk.CTkEntry(self.tab('Github Info'),placeholder_text='Paste Github URL here'),
      'cloneToggle': ctk.CTkSwitch(self.tab('Github Info'),text='Clone Repo?',onvalue=True,
                                   offvalue=False,command=self.cloneRepo)
    }

    row = 0
    column = 0
    columnspan = 1
    for name, field in self.inputs.items():
      field.grid(row=row,column=column,columnspan=columnspan,padx=5,pady=5,
                 sticky='nsew')
      row += 1
      if name in ('cloneURL','repoName'):
        if name == 'cloneURL':
          field.configure(state='disabled')
        column += 1
        row -= 1
      if name == 'editName':
        columnspan = 2
        column -= 1
      if name == 'repoURL':
        columnspan = 1


  def cloneRepo(self):
    fieldstate = 'normal' if self.inputs['cloneToggle'].get() == True else 'disabled'
    self.inputs['cloneURL'].configure(state=fieldstate)

  def renameRepo(self):
    if type(self.inputs['repoName']) == ctk.CTkLabel:
      self._firstRepoName = self.inputs["repoName"].cget('text')
    if self.inputs['editName'].get() == True:
      self.inputs['repoName'] = ctk.CTkEntry(self.tab('Github Info'),placeholder_text=self._firstRepoName)
      self.inputs['repoName'].grid(column=0,row=0,padx=5,pady=5,sticky='ew')
    else:
      self.inputs['repoName'] = ctk.CTkLabel(self.tab('Github Info'),text=self._firstRepoName,anchor='w')
      self.inputs['repoName'].grid(column=0,row=0,padx=5,pady=5,sticky='ew')
      self.inputs['repoURL'].configure(text=f'{self.gitURL}/{self.inputs["repoName"].cget("text")}'.replace(' ','-'))

    self.inputs['repoName'].bind("<Key>",self.labeller)

  def labeller(self,e):
    if e.keysym != 'BackSpace':
      self.inputs['repoURL'].configure(text=f'{self.gitURL}/{self.inputs["repoName"].get()}{e.char}'.replace(' ','-'))
    else:
      self.inputs['repoURL'].configure(text=f'{self.gitURL}/{self.inputs["repoName"].get()[:-1]}'.replace(' ','-'))