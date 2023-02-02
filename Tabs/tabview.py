import customtkinter
from Tabs.newProject import newProject

class tabView(customtkinter.CTkTabview):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)

        # create tabview
    self.newProject = newProject(tabview=self,tabname=' + ')