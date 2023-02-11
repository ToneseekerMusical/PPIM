import customtkinter
from tkinter import filedialog

class projectFrame(customtkinter.CTkFrame):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    #create project frame

    self.projectlabel = customtkinter.CTkLabel(
      self,
      text="Project Info",
      anchor="w")
    self.projectlabel.grid(
      row=0,
      column=0,
      padx=10,
      pady=5,
      sticky='w'
      )

    self.projectName = customtkinter.CTkEntry(
      self,
      placeholder_text='Project Name',
      )
    self.projectName.grid(
      row=1,
      column=0,
      columnspan=2,
      padx=(10, 5),
      pady=(5, 5),
      sticky="nsew"
      )

    self.UserName = customtkinter.CTkEntry(
      self,
      placeholder_text='User Name',
    )
    self.UserName.grid(
      row=2,
      column=0,
      padx=(10, 5),
      pady=(5, 5),
      sticky="nsew"
    )

    self.Password = customtkinter.CTkEntry(
      self,
      placeholder_text='Password',
      show="\u2022"
    )
    self.Password.grid(
      row=2,
      column=1,
      padx=(5,5),
      pady=(5,5),
      sticky="nsew"
    )

    self.selectPath = customtkinter.CTkButton(
      self,
      text='Choose Folder',
      command=self.select_Directory
    )
    self.selectPath.grid(
      row=4,
      column=1,
      padx=10,
      pady=5,
    )

    self.displayPath = customtkinter.CTkLabel(
      self,
      text='No directory selected'
    )
    self.displayPath.grid(
      row=4,
      column=0,
      padx=(10,5),
      pady=5,
      sticky="ew"
    )

  def select_Directory(self):
    path = filedialog.askdirectory(initialdir='/',title='Select PayloadCMS Instance Directory')
    self.displayPath.configure(text=path)
