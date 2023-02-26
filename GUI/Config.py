import os
import customtkinter as ctk
from Controllers.Setup import Setup
from GUI.Buttons.ExitBtn import ExitBtn

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.wm_title("AppWindow Test")
    self.attributes('-topmost',1)
    self.overrideredirect(True)
    # configure window
    self.title("Install")
    
    setup = Setup('config',mongoVer='base')
    setup.Config()

    self.label = ctk.CTkLabel(self,text='You must restart your computer for PPIM to function correctly')
    self.label.grid(row=0,column=0,columnspan=2,padx=10,pady=(10,5))

    self.exit = ExitBtn(self,self,text='Later')
    self.exit.grid(row=1,column=0,padx=10,pady=(10,5))

    self.restart = ctk.CTkButton(self,text='Restart Now',command = os.system("shutdown /r /t 1"))
    self.label.grid(row=1,column=1,padx=10,pady=(10,5))