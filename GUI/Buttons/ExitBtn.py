import customtkinter as ctk

class ExitBtn(ctk.CTkButton):
  def __init__(self,window:ctk.CTk,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self._command=window.destroy