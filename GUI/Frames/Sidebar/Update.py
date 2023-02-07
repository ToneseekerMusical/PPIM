import customtkinter as ctk
import GUI.Buttons.newWindow as newWin
import GUI.Frames.progress as updatewin
import GUI.Frames.paypal as Paypal
import GUI.Views.Settings as Settings

class updateFrame(ctk.CTkFrame):
  def __init__(self, *args, **kwargs):
    super().__init__(
      #bg_color='transparent',
      #fg_color='transparent',
      *args,
      **kwargs
      )

    self.grid_columnconfigure(0,weight=1)

    self.updateMongo=newWin.btn(
      master = self,
      text = 'Update MongoDB',
      frame = updatewin.progressFrame
    )
    self.updateMongo.grid(
      column=0,
      row=0,
      padx=10,
      pady=(10,5)
    )
    
    self.updateVSCode=newWin.btn(
      master = self,
      text = 'Update VS Code',
      frame = updatewin.progressFrame
    )
    self.updateVSCode.grid(
      column=0,
      row=1,
      padx=10,
      pady=5
    )
    
    self.updateNodeJS=newWin.btn(
      master = self,
      text = 'Update NodeJS',
      frame = updatewin.progressFrame
    )
    self.updateNodeJS.grid(
      column=0,
      row=2,
      padx=10,
      pady=5
    )
    
    self.updateCompass=newWin.btn(
      master = self,
      text = 'Update Compass',
      frame = updatewin.progressFrame
    )
    self.updateCompass.grid(
      column=0,
      row=3,
      padx=10,
      pady=5
    )
    
    self.updateGithub=newWin.btn(
      master = self,
      text = 'Update Github',
      frame = updatewin.progressFrame
    )
    self.updateGithub.grid(
      column=0,
      row=4,
      padx=10,
      pady=5
    )
    
    self.updatePPIM=newWin.btn(
      master = self,
      text = 'Update PPIM',
      frame = updatewin.progressFrame
    )
    self.updatePPIM.grid(
      column=0,
      row=5,
      padx=10,
      pady=5
    )
    
    self.updateAll=newWin.btn(
      master = self,
      text = 'Update updateAll',
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