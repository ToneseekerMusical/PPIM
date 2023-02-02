from tkinter import filedialog
import customtkinter
from Frames.sidebar import sidebarFrame
from Tabs.newProject import tabView

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
  def __init__(self):
    super().__init__()

    # configure window
    self.title("Python PayloadCMS Instance Manager")
    self.geometry(f"{1500}x{680}")
    customtkinter.set_appearance_mode('dark')

    # configure grid layout (4x4)
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure(2, weight=0)
    self.grid_rowconfigure(0, weight=1)

    #Create Side Bar
    self.sidebar = sidebarFrame(self)
    self.tabs = tabView(self)


if __name__ == "__main__":
  app = App()
  app.mainloop()