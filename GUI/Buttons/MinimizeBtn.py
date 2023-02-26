import customtkinter as ctk

class MinimizeBtn(ctk.CTkButton):
  def __init__(self,window:ctk.CTk,*args,**kwargs):
    super().__init__(text='U+1F5D5'*args,**kwargs)
    self._command=window.iconify