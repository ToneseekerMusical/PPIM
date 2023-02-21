import customtkinter as ctk
from pathlib import Path
from tkinter import filedialog

class dirSelect(ctk.CTkButton):
  def __init__(
    self,
    dep:str,
    dir:str,
    target:ctk.CTkBaseClass,
    *args,
    **kwargs):
    super().__init__(
      *args,
      **kwargs)
    self.cwd = f'{Path(dir)}'
    self.dep = dep
    self.target = target
    self._command=self.SelectDirectory
    self.windowOpen=False
    self.win=None

  def SelectDirectory(self):
    sitePath = filedialog.askdirectory(initialdir=f'{self.cwd}', title=f'Select {self.dep} Directory')
    self.target.configure(text=sitePath)