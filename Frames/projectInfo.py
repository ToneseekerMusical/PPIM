import customtkinter
from tkinter import filedialog

class projectFrame(customtkinter.CTk):
  def __init__(self, tab):
    super().__init__()
    #create project frame
    self.project_frame = customtkinter.CTkFrame(
      tab,
      corner_radius=0,
    )
    self.project_frame.grid(
      row=0,
      column=0,
      sticky='nsew'
    )
    self.project_frame.grid_columnconfigure((0,1), weight=1)

    self.projectlabel = customtkinter.CTkLabel(
      self.project_frame,
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
      self.project_frame,
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
      self.project_frame,
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
      self.project_frame,
      placeholder_text='Password',
    )
    self.Password.grid(
      row=2,
      column=1,
      padx=(5,5),
      pady=(5,5),
      sticky="nsew"
    )

    self.selectPath = customtkinter.CTkButton(
      self.project_frame,
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
      self.project_frame,
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
