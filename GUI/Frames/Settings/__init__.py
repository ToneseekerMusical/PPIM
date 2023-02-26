from .Accounts import Accounts
from .Directories import Directories
from .MongoDB import MongoDB
from .NodeJS import NodeJS
from .Payload import Payload
from .UI import UI
from .Updates import Updates

class Settings():
  def __init__(self) -> None:
    self.Accounts = Accounts
    self.Directories = Directories
    self.MongoDB = MongoDB
    self.NodeJS = NodeJS
    self.Payload = Payload
    self.UI = UI
    self.Updates = Updates