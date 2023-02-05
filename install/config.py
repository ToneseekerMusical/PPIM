import customtkinter as ctk
import sys
import os


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

    self.grid_columnconfigure(0,weight=1)

    self.label = ctk.CTkLabel(
      self,
      text='Getting things ready...',
      font=ctk.CTkFont(
        size=20,
        weight="bold"
        )
      )
    self.label.grid(
      row=0,
      column=0,
      padx=10,
      pady=10,
      sticky='nsew'
      )
  
    self.after(1000, self.restart)

  def restart(self):
    python = sys.executable
    os.execl(python, python, * sys.argv)
    #write version info to database and remove install directory