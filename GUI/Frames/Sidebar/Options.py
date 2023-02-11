import customtkinter as ctk
import GUI.Buttons.newWindow as newWin
import GUI.Frames.progress as updatewin
import GUI.Frames.paypal as Paypal
import GUI.Views.Settings as Settings

class OptionsFrame(ctk.CTkFrame):
  def __init__(self, *args, **kwargs):
    super().__init__(
      bg_color='transparent',
      fg_color='transparent',
      *args,
      **kwargs
      )
    
    self.updateAll=newWin.btn(
      master = self,
      text = 'Updates',
      frame = updatewin.progressFrame
    )
    self.updateAll.grid(
      column=0,
      row=6,
      padx=10,
      pady=5
    )

        #Settings
    self.settings = newWin.btn(
      master = self,
      text = 'Settings',
      frame = Settings.SettingsFrame
    )
    self.settings.grid(
      row=7,
      column=0,
      padx=10,
      pady=5,
      sticky='sew'
    )

    self.donate = newWin.btn(
      master = self,
      text = 'Donate',
      frame = Paypal.PaypalFrame
    )
    self.donate.grid(
      row=8,
      column=0,
      padx=10,
      pady=(5,10),
      sticky='sew'
    )