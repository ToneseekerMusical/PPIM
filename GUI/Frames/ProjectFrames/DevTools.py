import customtkinter as ctk
import subprocess, threading, os, signal, psutil

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
    self.startFrontend = ctk.CTkButton(self.tab('Dev Tools'),text='Start Frontend',
                                       command=lambda:self.NPMControl('frontend'))
    self.startFrontend.grid(row=0,column=0,padx=5,pady=5,sticky='ew')

    self.buildFrontend = ctk.CTkButton(self.tab('Dev Tools'),text='Build Frontend',
                                       command=lambda:self.BuildControl('frontend'))
    self.buildFrontend.grid(row=0,column=1,padx=5,pady=5,sticky='ew')

    self.startAdmin = ctk.CTkButton(self.tab('Dev Tools'),text='Start Admin',
                                    command=lambda:self.NPMControl('admin'))
    self.startAdmin.grid(row=1,column=0,padx=5,pady=5,sticky='ew')

    self.buildAdmin = ctk.CTkButton(self.tab('Dev Tools'),text='Build Admin',
                                    command=lambda:self.BuildControl('admin'))
    self.buildAdmin.grid(row=1,column=1,padx=5,pady=5,sticky='ew')

  def BuildControl(self,site):
    if site == 'admin':
      threading.Thread(target=self.AdminBuild).start()
      self.buildAdmin.configure(state='disabled')
    if site == 'frontend':
      threading.Thread(target=self.FrontendBuild).start()

  def FrontendBuild(self):
    print('Build Frontend')
    build = subprocess.run(['npm','--prefix',f'{self.frontend["frontendPath"]}','run','build'],
                           shell=True,capture_output=True,text=True)
    

  def AdminBuild(self):
    build = subprocess.Popen(['npm','--prefix',f'{self.frontend["adminPath"]}','run','build'],
                           shell=True,stdout=subprocess.PIPE,text=True)
#This SHOULD work on every command I want to pipe to a label to show the progress of a command
#     while not build.poll():
#      data = build.stdout.readline()
#      if data:
#        print(data)
#        #Configure Label here
#      else:
#        break
    self.buildAdmin.configure(state='normal')

  def NPMControl(self, site):
    self.npmThread = threading.Thread(target = lambda:self.NPMStart(site), daemon=True)
    self.npmThread.start()

  def NPMStart(self,site):
    if site == 'admin':
      self.stopAdmin = ctk.CTkButton(self.tab('Dev Tools'),text='Stop Admin',
                                     command=self.AdminStop)
      self.stopAdmin.grid(row=1,column=0,padx=5,pady=5,sticky='ew')
      self.admin = subprocess.Popen(['npm','--prefix',
                                    f'{self.frontend["adminPath"]}','run','dev'],shell=True)
    if site == 'frontend':
      self.stopFrontend = ctk.CTkButton(self.tab('Dev Tools'),text='Stop Frontend',
                                     command=self.FrontendStop)
      self.stopFrontend.grid(row=0,column=0,padx=5,pady=5,sticky='ew')
      self.front = subprocess.Popen(['npm','--prefix',
                                    f'{self.frontend["frontendPath"]}','run','dev'],shell=True)

  def AdminStop(self):
    currentProcess = psutil.Process(self.admin.pid)
    children = currentProcess.children(recursive=True)

    for child in children:
      child.terminate()

    self.startAdmin = ctk.CTkButton(self.tab('Dev Tools'),text='Start Admin',
                                    command=lambda:self.NPMControl('admin'))
    self.startAdmin.grid(row=1,column=0,padx=5,pady=5,sticky='ew')

  def FrontendStop(self):
    currentProcess = psutil.Process(self.frontend.pid)
    children = currentProcess.children(recursive=True)

    for child in children:
      child.terminate()

    self.startFrontend = ctk.CTkButton(self.tab('Dev Tools'),text='Start Admin',
                                    command=lambda:self.NPMControl('frontend'))
    self.startFrontend.grid(row=0,column=0,padx=5,pady=5,sticky='ew')