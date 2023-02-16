import customtkinter as ctk
import subprocess, threading

class devTools(ctk.CTkTabview):
  def __init__(self, frontend, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      segmented_button_selected_color=('#979DA2', 'gray29'),
      segmented_button_selected_hover_color=('#979DA2', 'gray29'),
      width=5,
      height=5,
      *args,
      **kwargs)
    #create shell frame
    self.add('Dev Tools')
    self.tab('Dev Tools').grid_columnconfigure((0,1),weight=1)
    self.startFrontend = ctk.CTkButton(self.tab('Dev Tools'),text='Start Frontend',command=threading.Thread(target=lambda:self.startFront(frontend['frontendPath'])).start)
    self.startFrontend.grid(row=0,column=0,padx=5,pady=5,sticky='ew')
    self.buildFrontend = ctk.CTkButton(self.tab('Dev Tools'),text='Build Frontend',command=threading.Thread(target=lambda:self.buildSite(frontend['frontendPath'])).start)
    self.buildFrontend.grid(row=0,column=1,padx=5,pady=5,sticky='ew')
    self.startAdmin = ctk.CTkButton(self.tab('Dev Tools'),text='Start Admin',command=threading.Thread(target=lambda:self.AdminStart(frontend['adminPath'])).start)
    self.startAdmin.grid(row=1,column=0,padx=5,pady=5,sticky='ew')
    self.buildAdmin = ctk.CTkButton(self.tab('Dev Tools'),text='Build Admin',command=threading.Thread(target=lambda:self.buildSite(frontend['adminPath'])).start)
    self.buildAdmin.grid(row=1,column=1,padx=5,pady=5,sticky='ew')

  def buildSite(self,siteDir):
    subprocess.Popen(['powershell','npm','run','build'],cwd=siteDir)

  def startFront(self,siteDir):
    self.front = subprocess.Popen(['powershell','npm','run','dev'],cwd=siteDir)
    self.stopFrontend = ctk.CTkButton(self.tab('Dev Tools'),text='Stop Frontend')
    self.stopFrontend.grid(row=0,column=0,padx=5,pady=5,sticky='ew')

  def AdminStart(self,siteDir):
    self.admin = subprocess.Popen(['powershell','npm','run','dev'],cwd=siteDir)
    self.stopAdmin = ctk.CTkButton(self.tab('Dev Tools'),text='Stop Admin')
    self.stopAdmin.grid(row=1,column=0,padx=5,pady=5,sticky='ew')
  
  def stopFront(self):...

  def AdminStop(self):...