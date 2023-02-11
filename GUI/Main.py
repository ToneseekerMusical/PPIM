import customtkinter as ctk
from GUI.Frames.sidebar import SidebarFrame
from Controllers.Mongo import MongoDB
from pymongo.database import Database

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
  def __init__(self, client:MongoDB, PPIM:Database):
    super().__init__()
    self.client = client
    self.PPIM = PPIM
    # configure window
    self.title("Python PayloadCMS Instance Manager")
    self.geometry(f"{1200}x{680}")
    ctk.set_appearance_mode('dark')

    # configure grid layout (4x4)
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure(2, weight=0)
    self.grid_rowconfigure(0, weight=1)

    #Create Side Bar
    self.sidebar = SidebarFrame(
      self.client,
      self,corner_radius=0,
      )
    self.sidebar.grid(
      row=0,
      column=0,
      sticky="ns"
      )
