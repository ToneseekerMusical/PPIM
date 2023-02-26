import customtkinter as ctk
from GUI.Buttons.ExitBtn import ExitBtn
from GUI.Frames.Reusable import ProgressFrame
from GUI.Buttons.DirSelectBtn import DirSelectBtn
import os, sys, threading

class InstallFrame(ctk.CTkFrame):
  def __init__(self,window:ctk.CTk,*args,**kwargs):
    super().__init__(bg_color='transparent',fg_color='transparent',*args,**kwargs)
    self.window = window
    
    self.mongoVer = 'base'

    self.columnconfigure((0,1,2), weight=1)
    self.cancel = ExitBtn(window,self,text='Cancel')
    self.cancel.grid(row=2,column=0,sticky='w')

    self.installbtn = ctk.CTkButton(self,text='Install',command=threading.Thread(target=self.StartInstall).start)
    self.installbtn.grid(row=2,column=2,sticky='e')

    self.dirSelect = DirSelectBtn('Select Install Path', 'C:\\', None, self)
    self.dirSelect.grid(row=1,column=0,sticky='w',pady=5)

    self.mongoVerSelect = ctk.CTkOptionMenu(self,values=['Base','Enterprise'],command=self.SetMongoVer)
    self.mongoVerSelect.grid(row=1,column=2,sticky='e',pady=5)

  def SetMongoVer(self,e:str):
    self.mongoVer = e.lower()

  def StartInstall(self):
    self.installbtn.configure(state='disabled')
    self.progress = ProgressFrame(self)
    self.progress.grid(row=0,column=0,columnspan=3,sticky='ew')
    self.progress.progress.start()
    if self.dirSelect.dir == None:
      self.dirSelect.dir = 'C:\\PPIM'
    from Controllers.Setup import Setup
    self.setup = Setup('install',self.dirSelect.dir,self.mongoVer)
    self.setup.Install()

    self.restart()
  
  def restart(self):
    python = sys.executable
    os.execl(python, python, * sys.argv)