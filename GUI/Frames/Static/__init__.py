from .InstallFrame import InstallFrame
from .NewProjectFrame import NewProjectFrame
from .ProjectFrame import ProjectFrame
from .SettingsFrame import SettingsFrame
from .SidebarFrame import SidebarFrame

class StaticFrames():
  def __init__(self) -> None:
    self.InstallFrame = InstallFrame
    self.NewProjectFrame = NewProjectFrame
    self.ProjectFrame = ProjectFrame
    self.SettingsFrame = SettingsFrame
    self.SidebarFrame = SidebarFrame