import customtkinter

class projectInfo(customtkinter.CTkFrame):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    #create shell frame
    
    self.projectName = customtkinter.CTkLabel(
      self,
      text='Project 1',
      font=customtkinter.CTkFont(
        size=20,
        weight="bold"
        )
    )
    self.projectName.grid(
      row=0,
      column=0,
      sticky='w'
    )

    self.userName = customtkinter.CTkEntry(
      self,
      #state='disabled'
    )
    self.userName.grid(
      row=1,
      column=0,
      sticky='w'
    )

    self.copyUser = customtkinter.CTkButton(
      self,
      text='Copy Username',
      command=self.copyFieldText(self.userName.get())
    )
    self.copyUser.grid(
      row=1,
      column=1
    )

    self.password = customtkinter.CTkEntry(
      self,
      show="\u2022",
      #state='disabled'
    )
    self.password.grid(
      row=2,
      column=0,
      sticky='w'
    )

    self.copyPass = customtkinter.CTkButton(
      self,
      text='Copy Password',
      command=self.copyFieldText(self.password)
    )
    self.copyPass.grid(
      row=2,
      column=1
    )

  def copyFieldText(field,*args):
    print(field)
