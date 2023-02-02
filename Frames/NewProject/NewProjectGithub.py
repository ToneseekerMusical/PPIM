import customtkinter

class githubFrame(customtkinter.CTkFrame):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
        #create github frame

    self.githublabel = customtkinter.CTkLabel(
      self,
      text="Github Info",
      anchor="w")
    self.githublabel.grid(
      row=0,
      column=0,
      padx=5,
      pady=5,
      sticky='w'
      )
    
    self.repositoryName = customtkinter.CTkEntry(
      self,
      placeholder_text='Repository Name'
    )
    self.repositoryName.grid(
      row=1,
      column=0,
      columnspan=3,
      padx=5,
      pady=5,
      sticky="nsew"
    )

    self.repoURL = customtkinter.CTkLabel(
      self,
      text='Your ropository URL will appear here'
    )
    self.repoURL.grid(
      row=2,
      column=0,
      columnspan=2,
      padx=5,
      pady=5,
      sticky='w'
    )

    self.openRepo = customtkinter.CTkButton(
      self,
      text='View on Github',
      command=self.viewRepo
    )
    self.openRepo.grid(
      row=2,
      column=2,
      padx=20,
      pady=5
    )

    self.cloneRepoURL = customtkinter.CTkEntry(
      self,
      placeholder_text='Paste the Github URL here'
    )
    self.cloneRepoURL.grid(
      row=3,
      column=0,
      columnspan=2,
      padx=5,
      pady=5,
      sticky="ew"
    )

    self.cloneRepoToggle = customtkinter.CTkSwitch(
      self,
      text='Clone Repo?',
      command=self.cloneRepoVal,
      onvalue="normal",
      offvalue="disabled"
    )
    self.cloneRepoToggle.grid(
      row=3,
      column=2,
      padx=20,
      pady=5
    )

    #Set Default Configuration
    self.cloneRepoURL.configure(state='disabled')

  def viewRepo(self):
    print('viewRepo')

  def cloneRepoVal(self):
    self.cloneRepoURL.configure(state=self.cloneRepoToggle.get())