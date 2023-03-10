import customtkinter as ctk
from GUI.Buttons.NewWindowBtn import NewWindowBtn
from GUI.Buttons.PaypalBtn import PaypalBtn
from GUI.Buttons.AppSettingsBtn import AppSettingsBtn
from GUI.Frames.ReusableFrames import ProgressFrame
from Controllers.Mongo import MongoDB

class OptionsFrame(ctk.CTkFrame):
  def __init__(self, PPIM:MongoDB, *args, **kwargs):
    super().__init__(bg_color='transparent',fg_color='transparent',*args,**kwargs)
    
    self.PPIM = PPIM

    self.updateAll=NewWindowBtn(
      master = self,
      text = 'Updates',
      frame = ProgressFrame
    )
    self.updateAll.grid(
      column=0,
      row=6,
      padx=10,
      pady=5
    )

    #Settings
    self.settings = AppSettingsBtn('Settings',self.PPIM,self, text='Settings')
    self.settings.grid(row=7,column=0,padx=10,pady=5,sticky='sew')

    self.donate = PaypalBtn(
      master = self
    )
    self.donate.grid(
      row=8,
      column=0,
      padx=10,
      pady=(5,10),
      sticky='sew'
    )