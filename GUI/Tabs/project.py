import customtkinter
from Frames.Projects.DBInfo import DBInfo
from Frames.Projects.Deploy import Deploy
from Frames.Projects.DevTools import devTools
from Frames.Projects.GithubInfo import github
from Frames.Projects.PluginManagement import pluginManager
from Frames.Projects.ProjectInfo import projectInfo
from Frames.Shell import shellFrame

class ProjectTab():
  def __init__(self,tabview:customtkinter.CTkTabview,tabname:str):
    super().__init__()
    tabview.grid(
      row=0,
      column=1,
      sticky="nsew")
    tabview.add(tabname)
    tabview.tab(tabname).grid_columnconfigure((0,1,2), weight=1)  # configure grid of individual tabs
    tabview.tab(tabname).grid_rowconfigure(2, weight=1)  # configure grid of individual tabs

    self.projectInfo = projectInfo(tabview.tab(tabname), corner_radius=0)
    self.projectInfo.grid(row=0,column=0,sticky='nsew')

    self.github = github(tabview.tab(tabname), corner_radius=0)
    self.github.grid(row=0,column=1,sticky='nsew')

    self.DBInfo = DBInfo(tabview.tab(tabname), corner_radius=0)
    self.DBInfo.grid(row=0,column=2,sticky='nsew')

    self.plugins = pluginManager(tabview.tab(tabname), corner_radius=0)
    self.plugins.grid(row=1,column=0,sticky='nsew')

    self.devTools = devTools(tabview.tab(tabname), corner_radius=0)
    self.devTools.grid(row=1,column=1,sticky='nsew')

    self.deploy = Deploy(tabview.tab(tabname), corner_radius=0)
    self.deploy.grid(row=1,column=2,sticky='nsew')

    #Create Shell Frame
    self.shell = shellFrame(tabview.tab(tabname), corner_radius=0)
    self.shell.grid(
      row=2,
      column=0,
      columnspan=3,
      sticky="nsew"
    )
    self.shell.grid_columnconfigure((0,1,2), weight = 1)
    self.shell.grid_rowconfigure(1,weight=1)