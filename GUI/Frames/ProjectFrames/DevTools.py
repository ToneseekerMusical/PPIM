import customtkinter as ctk
import multiprocessing, subprocess, threading

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
    self.frontend = frontend
    self.add('Dev Tools')
    self.tab('Dev Tools').grid_columnconfigure((0,1),weight=1)
    self.startFrontend = ctk.CTkButton(self.tab('Dev Tools'),text='Start Frontend',command=multiprocessing.Process(target=lambda:self.startFront(self.frontend['frontendPath']),daemon=True).start)
    self.startFrontend.grid(row=0,column=0,padx=5,pady=5,sticky='ew')
    self.buildFrontend = ctk.CTkButton(self.tab('Dev Tools'),text='Build Frontend',command=multiprocessing.Process(target=lambda:self.buildSite(self.frontend['frontendPath'])).start)
    self.buildFrontend.grid(row=0,column=1,padx=5,pady=5,sticky='ew')
    self.startAdmin = ctk.CTkButton(self.tab('Dev Tools'),text='Start Admin',command=threading.Thread(target=lambda: self.AdminStart(self.frontend['adminPath']),daemon=True).start)
    self.startAdmin.grid(row=1,column=0,padx=5,pady=5,sticky='ew')
    self.buildAdmin = ctk.CTkButton(self.tab('Dev Tools'),text='Build Admin',command=multiprocessing.Process(target=lambda:self.buildSite(self.frontend['adminPath'])).start)
    self.buildAdmin.grid(row=1,column=1,padx=5,pady=5,sticky='ew')

  def buildSite(self,siteDir):
    subprocess.Popen(['powershell','npm','run','build'],cwd=siteDir)

  def stopFront(self):
    self.front.__exit__()
    self.startFrontend = ctk.CTkButton(self.tab('Dev Tools'),text='Start Frontend',command=multiprocessing.Process(target=lambda:self.startFront(self.frontend['frontendPath']),daemon=True).start)
    self.startFrontend.grid(row=0,column=0,padx=5,pady=5,sticky='ew')
  
  def startFront(self,siteDir):
    self.front = multiprocessing.Process(['npm','run','dev'],cwd=siteDir)
    self.stopFrontend = ctk.CTkButton(self.tab('Dev Tools'),text='Stop Frontend',command=self.stopFront)
    self.stopFrontend.grid(row=0,column=0,padx=5,pady=5,sticky='ew')

  def AdminStart(self,siteDir):
    self.stopAdmin = ctk.CTkButton(self.tab('Dev Tools'),text='Stop Admin', command=self.AdminStop)
    self.stopAdmin.grid(row=1,column=0,padx=5,pady=5,sticky='ew')
    self.admin = multiprocessing.Process(target=subprocess.run(['powershell','npm','run','dev'],cwd=siteDir))
    self.admin.start()

  def AdminStop(self):
    self.admin.terminate()
    self.startAdmin = ctk.CTkButton(self.tab('Dev Tools'),text='Start Admin',command=threading.Thread(target=lambda: self.AdminStart(self.frontend['adminPath']),daemon=True).start)
    self.startAdmin.grid(row=1,column=0,padx=5,pady=5,sticky='ew')