import customtkinter

class githubFrame(customtkinter.CTk):
  def __init__(self, tab):
    super().__init__()
        #create github frame
    self.github_frame = customtkinter.CTkFrame(
      tab,
      corner_radius=0,
    )
    self.github_frame.grid(
      row=0,
      column=1,
      sticky='nsew'
    )
    self.github_frame.grid_columnconfigure((0,1,2), weight=1)

    self.githublabel = customtkinter.CTkLabel(
      self.github_frame,
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
      self.github_frame,
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
      self.github_frame,
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
      self.github_frame,
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
      self.github_frame,
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
      self.github_frame,
      text='Clone Repo?',
      command=self.cloneRepo
    )
    self.cloneRepoToggle.grid(
      row=3,
      column=2,
      padx=20,
      pady=5
    )

    #Set Default Configuration
    self.repoURL.configure(state='disabled')

  def viewRepo(self):
    print('viewRepo')

  def cloneRepo(self):
    print('cloneRepo')