from .Dependencies import Dependencies
from .Mongo import MongoCompass
from .Mongo import MongoDB
from .Mongo import MongoSH
from .NodeJS import NodeJS
from .Settings import Settings
from .Setup import Setup
from .SiteManagement import SiteManagement
from .System import System
from .Updates import Updates

class Controllers():
  def __init__(self) -> None:
    self.Dependencies = Dependencies
    self.MongoCompass = MongoCompass
    self.MongoDB = MongoDB
    self.MongoSH = MongoSH
    self.NodeJS = NodeJS
    self.Settings = Settings
    self.Setup = Setup
    self.SiteManagement = SiteManagement
    self.System = System
    self.Updates = Updates