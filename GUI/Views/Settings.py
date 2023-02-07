import customtkinter as ctk

class SettingsFrame(ctk.CTkFrame):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)

    self.appearance_mode_optionemenu = ctk.CTkOptionMenu(
      self, 
      values=["Light", "Dark", "System"],
      command=self.change_appearance_mode_event
      )
    self.appearance_mode_optionemenu.grid(
      row=2,
      column=0,
      padx=20,
      pady=(10, 10)
      )

    self.scaling_label = ctk.CTkLabel(
      self,
      text="UI Scaling:",
      anchor="w")
    self.scaling_label.grid(
      row=3,
      column=0,
      padx=20,
      pady=(10, 0)
      )

    self.scaling_optionemenu = ctk.CTkOptionMenu(
      self,
      values=["80%", "90%", "100%", "110%", "120%"],
      command=self.change_scaling_event
      )
    self.scaling_optionemenu.grid(
      row=4,
      column=0,
      padx=20,
      pady=(10, 20)
      )
    
  def change_appearance_mode_event(self, new_appearance_mode: str):
    ctk.set_appearance_mode(new_appearance_mode)

  def change_scaling_event(self, new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    ctk.set_widget_scaling(new_scaling_float)