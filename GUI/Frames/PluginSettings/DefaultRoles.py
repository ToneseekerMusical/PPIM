import customtkinter as ctk

class DefaultRoles(ctk.CTkFrame):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.name = 'Auth0'
    print(self.name)