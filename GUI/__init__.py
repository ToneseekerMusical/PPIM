from .Buttons import Buttons
from .Frames import Frames
from .Views import Views
from .Config import App as Config
from .Install import App as Install
from .Main import App as Main

class GUI():
  def __init__(self):
    self.Buttons = Buttons
    self.Frames = Frames
    self.Views = Views
    self.Config = Config
    self.Install = Install
    self.Main = Main