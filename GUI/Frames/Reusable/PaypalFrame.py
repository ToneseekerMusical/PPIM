import customtkinter as ctk
from GUI.Buttons.PaypalBtn import PaypalBtn

class PaypalFrame(ctk.CTkFrame):
  def __init__(self,*args,**kwargs):
    super().__init__(bg_color='transparent',fg_color='transparent',*args,**kwargs)
    self.grid_columnconfigure(0,weight=1)
    
    self.cta1 = ctk.CTkLabel(self,text='This tool will always have a free version for personal use, however,',)
    self.cta1.grid(row=0,sticky='ew')
    
    self.cta2 = ctk.CTkLabel(self,text='if you like it, please consider donating to its development.',)
    self.cta2.grid(row=1,sticky='ew')
    
    self.paypal = PaypalBtn(self)
    self.paypal.grid(row=2,)