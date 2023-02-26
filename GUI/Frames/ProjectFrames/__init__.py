from .DBInfo import databaseInfo
from .DevTools import devTools
from .EditSite import siteSetup
from .Github import Github
from .PluginManagement import pluginManager
from .ProjectInfo import projectInfo

class ProjectFrames():
  def __init__(self):
    self.DBInfo = databaseInfo
    self.DevTools = devTools
    self.EditSite = siteSetup
    self.Github = Github
    self.PluginManagement = pluginManager
    self.ProjectInfo = projectInfo