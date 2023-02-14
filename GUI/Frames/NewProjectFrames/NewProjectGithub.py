import customtkinter as ctk

class githubFrame(ctk.CTkTabview):
  def __init__(self, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      width=5,
      height=5,
      *args,
      **kwargs
      )
    
    self.add('Github Info')

    self.inputs = {
      'repoName': ctk.CTkEntry(self.tab('Github Info'),placeholder_text='Repository Name'),
      'repoURL': ctk.CTkLabel(self.tab('Github Info'),anchor='w',text='Repo Url will appear here'),
      'cloneURL': ctk.CTkEntry(self.tab('Github Info'),placeholder_text='Paste Github URL here'),
      'cloneToggle': ctk.CTkSwitch(self.tab('Github Info'),text='Clone Repo?',onvalue=True,
                                   offvalue=False,command=self.cloneRepo)
    }

    self.row = 0
    self.column = 0
    self.span = 2
    for name, field in self.inputs.items():
      field.grid(row=self.row,column=self.column,columnspan=self.span,padx=5,pady=5,
                 sticky='nsew')
      if name == 'repoURL':
        self.span = 1
      if name == 'cloneURL':
        field.configure(state='disabled')
        self.column += 1
        self.row -= 1
      self.row += 1

  def viewRepo(self):
    print('viewRepo')

  def cloneRepo(self):
    fieldstate = 'normal' if self.inputs['cloneToggle'].get() == True else 'disabled'
    self.inputs['cloneURL'].configure(state=fieldstate)