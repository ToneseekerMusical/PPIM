from .ArrayFrame import ArrayFrame
from .PaypalFrame import PaypalFrame
from .ProgressFrame import ProgressFrame
from .ShellFrame import ShellFrame

class ReusableFrames():
  def __init__(self) -> None:
    self.ArrayFrame = ArrayFrame
    self.PaypalFrame = PaypalFrame
    self.ProgressFrame = ProgressFrame
    self.ShellFrame = ShellFrame