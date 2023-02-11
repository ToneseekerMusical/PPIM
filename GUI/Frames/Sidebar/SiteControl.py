import customtkinter as ctk
from Controllers.Mongo import MongoDB
from GUI.Frames.NewProject import NewProjectFrame

class SiteControl(ctk.CTkFrame):
  def __init__(self,client:MongoDB,main:ctk.CTk,*args,**kwargs):
    super().__init__(
      bg_color='transparent',
      fg_color='transparent',
      *args,
      **kwargs
    )
    self.sites = client.dbList
    self.main = main

    print(f'The database list is: {self.sites}')
    if self.sites != []:
      self.selectLabel = ctk.CTkLabel(
        self,
        text='Select a Site'
      )
      self.selectLabel.grid(
        row = 0,
        column = 0,
        padx = 10,
        pady = 5,
        sticky = 'ew'
      )
      self.siteSelect = ctk.CTkOptionMenu(
        self,
        values=self.sites,
        command=self.DisplaySite
      )
      self.siteSelect.grid(
        row = 1,
        column = 0,
        padx = 10,
        pady = 5,
        sticky = 'ew'
      )

      self.addSiteBtn = ctk.CTkButton(
        self,
        text = 'Delete Site',
        command = self.DeleteSite
      )
      self.addSiteBtn.grid(
        row = 2,
        column = 0,
        padx = 10,
        pady = 5,
        sticky = 'ew'
      )
    
      self.addSiteBtn = ctk.CTkButton(
        self,
        text = 'New Site',
        command = self.AddSite
      )
      self.addSiteBtn.grid(
        row = 3,
        column = 0,
        padx = 10,
        pady = 5,
        sticky = 'ew'
      )
    else:
      self.AddSite()

  def DisplaySite(self,site):
    print(f'Displaying {site}')

  def AddSite(self):
    self.newProject = NewProjectFrame(
      self.main
    )
    self.newProject.grid(
      row = 0,
      column = 1,
      sticky = 'nsew'
    )

  def DeleteSite(self):
    print(f'Deleting {self.siteSelect.get()}')