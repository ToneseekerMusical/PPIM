from .AppSettingsBtn import AppSettingsBtn
from .DirSelectBtn import DirSelectBtn
from .ExitBtn import ExitBtn
from .MinimizeBtn import MinimizeBtn
from .PaypalBtn import PaypalBtn
from .NewWindowBtn import NewWindowBtn
from .PluginSettings import PluginSettingsBtn
from .PluginSettings import PluginSettingsSwitch

class Buttons():
  def __init__(self):
    self.AppSettingsBtn = AppSettingsBtn
    self.dirSelectBtn = DirSelectBtn
    self.exit = ExitBtn
    self.minimize = MinimizeBtn
    self.paypal = PaypalBtn
    self.newWindow = NewWindowBtn
    self.pluginButton = PluginSettingsBtn
    self.pluginSwitch = PluginSettingsSwitch