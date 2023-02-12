import customtkinter as ctk

class btn(ctk.CTkButton):
  def __init__(
    self,
    *args,
    frame:ctk.CTkFrame,
    **kwargs):
    super().__init__(
      *args,
      **kwargs)
    self._command=self.open
    self.windowOpen=False
    self.win=None
    self.frame = frame

  def open(self):
    if self.windowOpen == False:
      self.win = ctk.CTkToplevel(self)
      self.win.title('Python Payload Instance Manager')
      self.win.geometry("400x300")
      self.win.protocol('WM_DELETE_WINDOW',self.close)

      # create label on CTkToplevel window
      self.frame = self.frame(self.win)
      self.frame.pack(side="top", fill="both", expand=True, padx=10, pady=10)
      self.windowOpen=True
      self.configure(state='disabled')

  def close(self):
    if self.windowOpen == True:
      self.windowOpen = False
      self.configure(state='normal')
      self.win.destroy()