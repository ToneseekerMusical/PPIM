import customtkinter as ctk
import GUI.Buttons.exit as Exit
import GUI.Frames.progress as Progress
import os, sys

class InstallFrame(ctk.CTkFrame):
  def __init__(
      self,
      window:ctk.CTk,
      *args,
      **kwargs):
    super().__init__(
      bg_color='transparent',
      fg_color='transparent',
      *args,
      **kwargs
      )
    self.window = window
    self.columnconfigure((0,1), weight=1)
    self.cancel = Exit.ExitButton(
      window,
      self,
      text='Cancel'
    )
    self.cancel.grid(
      row=1,
      column=0,
      sticky='w'
    )

    self.installbtn = ctk.CTkButton(
       self,
       text='Install',
       command=self.startInstall
    )
    self.installbtn.grid(
      row=1,
      column=1,
      sticky='e'
    )

  def startInstall(self):
    from Controllers.Setup import Setup
    self.installbtn.configure(state='disabled')
    self.progress = Progress.progressFrame(
      self,
    )
    self.progress.grid(
      row=0,
      column=0,
      columnspan=2,
      sticky='ew'
    )
    self.progress.progress.start()
    setup = Setup('install')
    setup.StartSetup()
    python = sys.executable
    os.execl(python, python, * sys.argv)