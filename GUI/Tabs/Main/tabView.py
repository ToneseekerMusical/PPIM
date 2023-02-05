import customtkinter
import GUI.Tabs.Sub.newProject as newProject
import GUI.Tabs.Sub.project as ProjectTab

class tabView(customtkinter.CTkTabview):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)

        # create tabview
    self.tablist = {
      'Project1': ProjectTab.ProjectTab(self,'Project 1'),
      'New Project': newProject.newProject(self,' + ')
    }

    