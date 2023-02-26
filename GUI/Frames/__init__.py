from .NewProjectFrames import NewProjectFrames
from .ProjectFrames import ProjectFrames
from .PluginSettings import PluginSettings
from .Settings import Settings
from .Sidebar import SidebarFrames
from .Static import StaticFrames
from .Reusable import ReusableFrames

class Frames():
  def __init__(self):
    self.StaticFrames = StaticFrames
    self.ReusableFrames = ReusableFrames
    self.SettingsFrame = Settings
    self.NewProjectFrames = NewProjectFrames
    self.ProjectFrames = ProjectFrames
    self.PluginSettings = PluginSettings
    self.SidebarFrames = SidebarFrames