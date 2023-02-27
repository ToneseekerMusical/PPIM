import os
import customtkinter as ctk
from Controllers.Setup import Setup
from GUI.Buttons.ExitBtn import ExitBtn
from pathlib import Path

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.wm_title("AppWindow Test")
    self.attributes('-topmost',1)
    self.overrideredirect(True)
    self.iconbitmap(default=f'{Path().cwd()}\payload.ico')
    # configure window
    self.title("Install")
    
    setup = Setup('config',mongoVer='base')
    setup.Config()

    self.label = ctk.CTkLabel(self,text='Configuration complete, please re-launch PPIM')
    self.label.grid(row=0,column=0,columnspan=2,padx=10,pady=(10,5))

    self.exit = ExitBtn(self,self,text='Ok')
    self.exit.grid(row=1,column=0,padx=10,pady=(10,5))