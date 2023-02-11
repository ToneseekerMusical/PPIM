import customtkinter as ctk
import GUI.Buttons.exit as Exit
import GUI.Frames.progress as Progress
import os, sys, threading

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
       command=threading.Thread(target=self.StartInstall).start
    )
    self.installbtn.grid(
      row=1,
      column=1,
      sticky='e'
    )

  def StartInstall(self):
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
    from Controllers.Setup import Setup
    self.setup = Setup('install',mongoVer='base')
    self.setup.Install()
    
    self.restart()
  
  def restart(self):
    python = sys.executable
    os.execl(python, python, * sys.argv)