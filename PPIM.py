import customtkinter as ctk
from Controllers.Mongo import MongoDB
from Controllers.System import System
import ctypes, sys
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
    
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
      ppim = None
      systemInfo = None

    mongo = System().get_service('MongoDB')
    
    if ppim != None and systemInfo != None:
      from GUI.Main import App
      app = App(client,ppim)
    elif mongo != None and systemInfo == None:
      from GUI.Config import App
      app = App()
    else:
      from GUI.Install import App
      app = App()

    app.eval('tk::PlaceWindow . center')

    ctypes.windll.shell32.ShellExecuteW(None, "runas", app.mainloop(), " ".join(sys.argv), None, 1)