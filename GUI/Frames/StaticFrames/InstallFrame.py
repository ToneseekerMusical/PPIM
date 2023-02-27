import customtkinter as ctk
from GUI.Buttons.ExitBtn import ExitBtn
from GUI.Frames.ReusableFrames.ProgressFrame import ProgressFrame
import os, sys, threading
from pathlib import Path

class InstallFrame(ctk.CTkFrame):
  def __init__(self,window:ctk.CTk,*args,**kwargs):
    super().__init__(bg_color='transparent',fg_color='transparent',*args,**kwargs)
    self.window = window
    if Path(f"{Path().cwd()}\lib\\").exists():
      self.instText = 'Configure'
    else:
      self.instText = 'Download'
    self.mongoVer = 'base'

    self.columnconfigure((0,1,2), weight=1)
    self.cancel = ExitBtn(window,self,text='Cancel')
    self.cancel.grid(row=2,column=0,sticky='w')

    self.installbtn = ctk.CTkButton(self,text=self.instText,command=threading.Thread(target=self.Install).start)
    self.installbtn.grid(row=2,column=2,sticky='e')

    self.mongoVerSelect = ctk.CTkOptionMenu(self,values=['Base','Enterprise'],command=self.SetMongoVer)
    self.mongoVerSelect.grid(row=2,column=1,sticky='ew',padx=10)

  def SetMongoVer(self,e:str):
    self.mongoVer = e.lower()

  def Install(self):
    self.installbtn.configure(state='disabled')
    self.progress = ProgressFrame(self)
    self.progress.grid(row=0,column=0,columnspan=3,sticky='ew')
    self.progress.progress.start()
    from Controllers.Setup import Setup
    self.setup = Setup('install',Path().cwd(),self.mongoVer)
    self.setup.Install()
    self.installbtn.configure(command=self.Restart,text='Configure',state='normal')

  def Restart(self):
    python = sys.executable
    os.execl(python,python, * sys.argv)