import customtkinter as ctk

class ProgressFrame(ctk.CTkFrame):
  def __init__(self,*args,**kwargs):
    super().__init__(bg_color='transparent',fg_color='transparent',*args,**kwargs)

    self.grid_columnconfigure(0,weight=1)

    self.progress = ctk.CTkProgressBar(self,mode='indeterminate')
    self.progress.grid(row=0,column=0,pady=(0,10),sticky='ew')

    self.readout = ctk.CTkLabel(self,text='Readout')
    self.readout.grid(row=1,column=0,pady=(0,10))