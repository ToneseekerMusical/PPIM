import customtkinter as ctk

class PaypalButton(ctk.CTkButton):
  def __init__(
    self,
    *args,
    **kwargs):
    super().__init__(
      text = 'Donate',
      *args,
      **kwargs)
    self._command=self.donate
    self.donateopen=False
    self.win=None

  def donate(self):
    if self.donateopen == False:
      self.win = ctk.CTkToplevel(self)
      self.win.geometry("400x200")
      self.win.protocol('WM_DELETE_WINDOW',self.openCheck)

      # create label on CTkToplevel window
      label = ctk.CTkLabel(self.win, text="CTkToplevel window")
      label.pack(side="top", fill="both", expand=True, padx=40, pady=40)
      self.donateopen=True
      self.configure(state='disabled')

  def openCheck(self):
    if self.donateopen == True:
      self.donateopen = False
      self.configure(state='normal')
      self.win.destroy()
