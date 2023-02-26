import customtkinter as ctk
import webbrowser

class PaypalBtn(ctk.CTkButton):
  def __init__(self,*args,**kwargs):
    super().__init__(text = 'Donate',*args,**kwargs)
    self._command=self.donate
    self.donateopen=False
    self.win=None

  def donate(self):
    webbrowser.open('https://www.paypal.com/donate/?hosted_button_id=GLR6WE9HS9PZL')

  def openCheck(self):
    if self.donateopen == True:
      self.donateopen = False
      self.configure(state='normal')
      self.win.destroy()
