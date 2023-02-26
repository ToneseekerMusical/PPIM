from .SiteManagementFrame import SiteManagementFrame
from .MongoFrame import MongoFrame
from .OptionsFrame import OptionsFrame

class SidebarFrames():
  def __init__(self):
    self.SiteControl = SiteManagementFrame
    self.Mongo = MongoFrame
    self.Options = OptionsFrame