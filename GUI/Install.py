import customtkinter as ctk
from pathlib import Path
from GUI.Frames.StaticFrames.InstallFrame import InstallFrame
from GUI.Frames.ReusableFrames.PaypalFrame import PaypalFrame


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

    self.grid_columnconfigure(0,weight=1)

    self.label = ctk.CTkLabel(self,text='PayloadCMS Instance Manager',font=ctk.CTkFont(size=20,weight="bold"))
    self.label.grid(row=0,column=0,padx=10,pady=10,sticky='nsew')
    
    self.paypal = PaypalFrame(self,)
    self.paypal.grid(row=1,column=0,columnspan=2,padx=10,sticky='ew')

    self.install = InstallFrame(self,self,)
    self.install.grid(row=2,column=0,padx=10,pady=10,sticky='ew')
