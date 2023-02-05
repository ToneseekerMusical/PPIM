import customtkinter as ctk
import pathlib

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.after(10, self.set_appwindow, self)

  def set_appwindow(self):
    from ctypes import windll
    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080
    hwnd = windll.user32.GetParent(self.winfo_id())
    style = windll.user32.GetWindowLongPtrW(hwnd, GWL_EXSTYLE)
    style = style & ~WS_EX_TOOLWINDOW
    style = style | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongPtrW(hwnd, GWL_EXSTYLE, style)
    # re-assert the new window style
    self.withdraw()
    self.after(10, self.deiconify)
    
if __name__ == "__main__":
  path = pathlib.Path
  cwd = str(path.cwd())
  #if path(cwd+'\\Install').exists():
  #    if not path(cwd+'\\Install\\setup.ppimcfg').exists():
  #      import Install.install as inst
  #      app = inst.App()
  #    else:
  #      import Install.config as config
  #      app = config.App()
  #else: 
  #  app=App()
  import GUI.Views.Main as Main
  app = Main.App()
  app.eval('tk::PlaceWindow . center')
  app.mainloop()