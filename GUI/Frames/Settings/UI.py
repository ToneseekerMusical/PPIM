import customtkinter as ctk

class UI(ctk.CTkFrame):
  def __init__(self,*args,**kwargs):
    super().__init__(bg_color='transparent',fg_color='transparent',*args,**kwargs)
    self.grid_columnconfigure((0,1),weight=1)
    appearance =["Light", "Dark", "System"]
    scaling=["80%", "90%", "100%", "110%", "120%"]
    self.form = {
      'labels':{
        'appearance':ctk.CTkLabel(self, text="Appearance Mode:", anchor="w"),
        'scaling':ctk.CTkLabel(self, text="UI Scaling:", anchor="w")
      },
      'inputs':{
        'appearance':ctk.CTkOptionMenu(self,values=appearance,command=self.changeAppearance),
        'scaling':ctk.CTkOptionMenu(self, values=scaling,command=self.changeScaling),
      }
    }

    row = 0
    column = 0
    for group, fields in self.form.items():
      fields:dict
      for field in fields.keys():
        f:ctk.CTkBaseClass = self.form[group][field]
        f.grid(row=row, column=column, padx=5, pady=5,sticky='nsew')
        row += 1
      column += 1
      row = 0
  
  def changeAppearance(self, new_appearance_mode: str):
      ctk.set_appearance_mode(new_appearance_mode)

  def changeScaling(self, new_scaling: str):
      new_scaling_float = int(new_scaling.replace("%", "")) / 100
      ctk.set_widget_scaling(new_scaling_float)
      ctk.set_window_scaling(new_scaling_float)