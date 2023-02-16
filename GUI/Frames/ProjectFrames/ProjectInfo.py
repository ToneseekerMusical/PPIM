import customtkinter as ctk
import webbrowser
from pymongo.database import Database
import subprocess

class projectInfo(ctk.CTkTabview):
  def __init__(self, frontendInfo, db:Database, site, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      width=5,
      height=5,
      *args,
      **kwargs)
    #create shell frame
    self.add('Site Info')
    self.add('Edit')
    self.tab('Site Info').grid_columnconfigure((0,1),weight=1)
    self.tab('Edit').grid_columnconfigure((0,1),weight=1)
    self.site = site
    self.db = db
    self.frontendInfo = frontendInfo
    self.frontendHost = self.frontendInfo['frontendHost']
    self.frontendPort = self.frontendInfo['frontendPort']
    self.adminHost = self.frontendInfo['adminHost']
    self.adminPort = self.frontendInfo['adminPort']

    self.tabs = {
      'Site Info':{
        'labels':{
          'frontendURLLabel':ctk.CTkLabel(self.tab('Site Info'),text='Frontend Site:',anchor='w'),
          'adminURLLabel':ctk.CTkLabel(self.tab('Site Info'),text='Admin Site:',anchor='w'),
          'nodeLabel':ctk.CTkLabel(self.tab('Site Info'),text='Node Version:',anchor='w'),
          'frontendCodeLabel':ctk.CTkLabel(self.tab('Site Info'),text='Frontend Code:',anchor='w'),
          'adminCodeLabel':ctk.CTkLabel(self.tab('Site Info'),text='Admin Code:',anchor='w'),
        },
        'inputs':{
          'FrontendURL': ctk.CTkButton(self.tab('Site Info'),text='Open in Browser',command=lambda:self.OpenURL('frontend')),
          'AdminURL': ctk.CTkButton(self.tab('Site Info'),text='Open in Browser',command=lambda:self.OpenURL('admin')),
          'NodeVersion': ctk.CTkLabel(self.tab('Site Info'),text=self.frontendInfo['nodeJSversion'],anchor='w'),
          'FrontendBtn': ctk.CTkButton(self.tab('Site Info'),text='Open in VS Code',command=lambda:self.OpenCode(self.frontendInfo['frontendPath'])),
          'AdminBtn': ctk.CTkButton(self.tab('Site Info'),text='Open in VS Code',command=lambda:self.OpenCode(self.frontendInfo['adminPath'])),
        }
      },
      'Edit':{
        'labels':{
          'FrontendURLLabel': ctk.CTkLabel(self.tab('Edit'),text='Edit Frontend URL:',anchor='w'),
          'FrontendPortLabel': ctk.CTkLabel(self.tab('Edit'),text='Edit Frontend Port:',anchor='w'),
          'AdminURLLabel': ctk.CTkLabel(self.tab('Edit'),text='Edit Admin URL:',anchor='w'),
          'AdminPortLabel': ctk.CTkLabel(self.tab('Edit'),text='Edit Admin Port:',anchor='w'),
        },
        'inputs':{
          'FrontendHost':ctk.CTkEntry(self.tab('Edit'),placeholder_text=self.frontendHost),
          'FrontendPort':ctk.CTkEntry(self.tab('Edit'),placeholder_text=self.frontendPort),
          'AdminHost':ctk.CTkEntry(self.tab('Edit'),placeholder_text=self.adminHost),
          'AdminPort':ctk.CTkEntry(self.tab('Edit'),placeholder_text=self.adminPort),
          'Submit': ctk.CTkButton(self.tab('Edit'),text='Submit',command=self.updateHost),
        }
      }}

    row = 0
    column = 0
    for tab, groups in self.tabs.items():
      for group, fields in groups.items():
        for field in fields.keys():
          self.tabs[tab][group][field].grid(row=row,column=column,padx=5,pady=5,sticky='ew')
          row += 1
        row = 0
        column += 1
      row = 0
      column = 0

  def OpenURL(self,name):
    webbrowser.open(f'{getattr(self,f"{name}Host")}:{self.frontendInfo[f"{name}Port"]}',2)
  
  def updateHost(self):
    if self.tabs['Edit']['inputs']['FrontendHost'].get() != '':
      self.frontendHost = self.tabs['Edit']['inputs']['FrontendHost'].get()
    if self.tabs['Edit']['inputs']['FrontendPort'].get() != '':
      self.frontendPort = self.tabs['Edit']['inputs']['FrontendPort'].get()
    if self.tabs['Edit']['inputs']['AdminHost'].get() != '':
      self.adminHost = self.tabs['Edit']['inputs']['AdminHost'].get()
    if self.tabs['Edit']['inputs']['AdminPort'].get() != '':
      self.adminPort = self.tabs['Edit']['inputs']['AdminPort'].get()
    
    document = {
      '$set':{
        'frontend.frontendPort':self.frontendPort,
        'frontend.frontendHost':self.frontendHost,
        'frontend.adminPort':self.adminPort,
        'frontend.adminHost':self.adminHost
        }
      }

    self.db.get_collection('Site Info').update_one({'_id':self.site},update=document)


  def OpenCode(self,path):
    subprocess.run(['code',f'{path}'])