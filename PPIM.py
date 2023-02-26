import customtkinter as ctk
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
      client = MongoDB()
      client.StartService()
      client.Connect(
        "mongodb://localhost:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=PPIM",
        )
      ppim = client.Connect(dbName='PPIM')
      try:
        systemInfo = ppim.get_collection('System').find_one()
      except:
        systemInfo = None
    except:
      print('Database not available!')
      ppim = None
      systemInfo = None

    if ppim != None and systemInfo != None:
      from GUI import Main
      app = Main(client,ppim)
    elif ppim != None and systemInfo == None:
      from GUI import Config
      app = Config()
    else:
      from GUI import Install
      app = Install()

    app.eval('tk::PlaceWindow . center')

    ctypes.windll.shell32.ShellExecuteW(None, "runas", app.mainloop(), " ".join(sys.argv), None, 1)