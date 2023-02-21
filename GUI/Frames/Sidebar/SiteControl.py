import customtkinter as ctk
from GUI.Frames.newproject import NewProjectFrame
from GUI.Frames.project import ProjectFrame
from Controllers.Mongo import MongoDB
from pymongo.database import Database
from pathlib import Path
import shutil

class SiteControl(ctk.CTkFrame):
  def __init__(self,main:ctk.CTk,client:MongoDB,PPIM:Database,*args,**kwargs):
    super().__init__(
      bg_color='transparent',
      fg_color='transparent',
      *args,
      **kwargs
    )

    self.client = client
    self.PPIM = PPIM
    self.dbList = self.client.dbList
    print(self.dbList)

    if self.dbList == []:
      self.dbList = ['No sites found']
    self.main = main

    self.selectLabel = ctk.CTkLabel(self,text='Select a Site')
    self.selectLabel.grid(row=0,column=0,padx=10,pady=5,sticky='ew')
    
    self.siteSelect = ctk.CTkOptionMenu(self,values=self.dbList,command=self.DisplaySite)
    self.siteSelect.grid(row=1,column=0,padx=10,pady=5,sticky='ew')
    
    self.SiteManagement()

  def DisplaySite(self,site):
    self.project = ProjectFrame(self.client,site,self.main)
    self.project.grid(row=0,column=1,sticky='nsew')
  
  def AddSite(self):
    self.newProject = NewProjectFrame(self.client,self.PPIM,self.main)
    self.newProject.grid(row=0,column=1,sticky='nsew')
    self.newProject.bind('<Unmap>',self.RefreshDisplay)
  
  def SiteManagement(self):
    if self.dbList != ['No sites found']:
      self.DisplaySite(self.dbList[0])
    
      self.delSiteBtn = ctk.CTkButton(self,text = 'Delete Site',command = self.DeleteSite)
      self.delSiteBtn.grid(row=2,column=0,padx=10,pady=5,sticky='ew')
    
      self.addSiteBtn = ctk.CTkButton(self,text='New Site',command=self.AddSite)
      self.addSiteBtn.grid(row=3,column=0,padx=10,pady=5,sticky='ew')
    else:
      self.AddSite()

  def RefreshDisplay(self, e=None):
    dbList = self.dbList
    self.client.RefreshServer()
    self.dbList = self.client.dbList
    self.siteSelect.configure(values=self.dbList)
    newSite = list(set(self.dbList) - set(dbList))[0]
    self.DisplaySite(newSite)
    self.siteSelect.set(newSite)
    self.SiteManagement()

  def DeleteSite(self):
    if len(self.dbList) > 0:
      self.client.DeleteDatabase(self.siteSelect.get())
      self.PPIM.get_collection('Sites').find_one_and_delete({'_id':self.siteSelect.get()})
      self.client.RefreshServer()
      self.dbList = self.client.dbList
      self.siteSelect.configure(values=self.dbList)
      path = Path(f'{Path.cwd()}\\websites\\{self.siteSelect.get()}')
      shutil.rmtree(f'{path}')
      if len(self.dbList) > 0:
        self.DisplaySite(self.dbList[0])
        self.siteSelect.set(self.dbList[0])
      else:
        self.project.grid_remove()
        self.dbList = ['No sites found']
        self.siteSelect.set(self.dbList[0])
        self.delSiteBtn.destroy()
        self.addSiteBtn.destroy()
        self.AddSite()
        self.newProject.grid(row=0,column=1,sticky='nsew')
