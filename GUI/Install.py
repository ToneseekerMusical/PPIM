import customtkinter as ctk
import GUI.Frames.install as Install
import GUI.Frames.paypal as Paypal


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
      text='PayloadCMS Instance Manager',
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
    
    self.paypal = Paypal.PaypalFrame(
      self,
    )
    self.paypal.grid(
      row=1,
      column=0,
      columnspan=2,
      padx=10,
      sticky='ew'
    )

    self.install = Install.InstallFrame(
      self,
      self,
    )
    self.install.grid(
      row=2,
      column=0,
      padx=10,
      pady=10,
      sticky='ew'
    )
