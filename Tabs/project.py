import customtkinter
from Frames.githubInfo import githubFrame
from Frames.mongoDBInfo import mongoDBFrame
from Frames.plugins import pluginFrame
from Frames.projectInfo import projectFrame
from Frames.shell import shellFrame

class tabView(customtkinter.CTk):
  def __init__(self,window):
    super().__init__()
    