import customtkinter as ctk
from pathlib import Path
from tkinter import filedialog

class DirSelectBtn(ctk.CTkButton):
  def __init__(
    self,
    dep:str,
    dir:str,
    target:ctk.CTkBaseClass = None,
    *args,
    **kwargs):
    super().__init__(
      text=dep,
      *args,
      **kwargs)
    self.cwd = f'{Path(dir)}'
    self.dep = dep
    self.dir = None
    self.target = target
    self._command=self.SelectDirectory
    self.windowOpen=False
    self.win=None

  def SelectDirectory(self):
    sitePath = filedialog.askdirectory(initialdir=f'{self.cwd}', title=f'Select {self.dep} Directory')
    if self.target != None:
      self.target.configure(text=sitePath)
    else:
      self.dir = sitePath