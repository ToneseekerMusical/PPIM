import customtkinter as ctk
from pathlib import Path
from Controllers.Mongo import MongoDB
import ctypes, sys

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
if __name__ == "__main__":

    try:
      db = MongoDB()
      db.StartService()
      db.Connect(
        "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=PPIM",
        )
      ppim = db.Connect(dbName='PPIM')
      try:
        systemInfo = ppim.get_collection('System').find_one()
      except:
        systemInfo = None
    except:
      print('Database not available!')
      ppim = None
      systemInfo = None

    if systemInfo != None:
      import GUI.Main as Main
      app = Main.App(db,ppim)
    elif ppim != None:
      import GUI.Config as Config
      app = Config.App()
    else:
      import GUI.Install as Install
      app = Install.App()

    app.eval('tk::PlaceWindow . center')

    ctypes.windll.shell32.ShellExecuteW(None, "runas", app.mainloop(), " ".join(sys.argv), None, 1)