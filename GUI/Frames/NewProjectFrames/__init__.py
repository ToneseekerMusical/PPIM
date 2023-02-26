from .NewProjectBackendInfo import BackendFrame
from .NewProjectFrontendInfo import FrontendFrame
from .NewProjectGithub import GithubFrame
from .NewProjectInfo import ProjectFrame
from .NewProjectPlugins import PluginFrame

class NewProjectFrames():
  def __init__(self):
    self.BackendInfo = BackendFrame
    self.FrontendInfo = FrontendFrame
    self.Github = GithubFrame
    self.ProjectInfo = ProjectFrame
    self.Plugins = PluginFrame