import customtkinter
from Tabs.newProject import newProject
from Tabs.project import ProjectTab

class tabView(customtkinter.CTkTabview):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)

        # create tabview
    self.tablist = {
      'Project1': ProjectTab(self,'Project 1'),
      'New Project': newProject(self,' + ')
    }

    