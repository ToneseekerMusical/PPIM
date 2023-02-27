import customtkinter as ctk
from GUI.Frames.SidebarFrames.SidebarFrame import SidebarFrame
from Controllers.Mongo import MongoDB
from pymongo.database import Database
from pathlib import Path

ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
  def __init__(self, client:MongoDB, PPIM:Database):
    super().__init__()
    self.client = client
    self.PPIM = PPIM
    # configure window
    self.iconbitmap(default=f'{Path().cwd()}\payload.ico')
    self.title("Python PayloadCMS Instance Manager")
    width  = self.winfo_screenwidth()
    height = self.winfo_screenheight()
    self.geometry(f'{width/2}x{height/2}')
    ctk.set_appearance_mode('dark')
    self.resizable(False,False)
    # configure grid layout (4x4)
    self.grid_columnconfigure(0, weight=0)
    self.grid_columnconfigure(1, weight=1)
    self.grid_rowconfigure(0, weight=1)
    #Create Side Bar
    self.sidebar = SidebarFrame(
      self.client,
      self.PPIM,
      self,corner_radius=0,
      )
    self.sidebar.grid(
      row=0,
      column=0,
      sticky="nsw"
      )
