import customtkinter as ctk
from Controllers.Mongo import MongoDB as MongoDB
from Controllers.Mongo import MongoCompass as Compass
from Controllers.Mongo import MongoSH as MongoSH

class MongoFrame(ctk.CTkFrame):
  def __init__(self, client:MongoDB, *args, **kwargs):
    super().__init__(
      bg_color='transparent',
      fg_color='transparent',
      *args,
      **kwargs
      )
    
    self.client = client

    self.logo_label = ctk.CTkLabel(
      self,
      text="PPIM",
      font=ctk.CTkFont(
        size=20,
        weight="bold"
        )
      )
    self.logo_label.grid(
      row=0,
      column=0,
      padx=10,
      pady=(10, 5),
      sticky='new'
      )
    
    #management buttons

    self.startMongo = ctk.CTkButton(
      self,
      text='Start MongoDB',
      command=self.startMongoDB
      )
    self.startMongo.grid(
      row=1,
      column=0,
      padx=10,
      pady=5,
      sticky='ew'
      )

    self.stopMongo = ctk.CTkButton(
      self,
      text='Stop MongoDB',
      command=self.stopMongoDB
      )
    self.stopMongo.grid(
      row=2,
      column=0,
      padx=10,
      pady=5,
      sticky='ew'
      )

    self.MongoStatus = ctk.CTkButton(
      self,
      text='MongoDB: Off',
      text_color_disabled='black',
      fg_color='grey',
    )
    self.MongoStatus.grid(
      row=3,
      column=0,
      padx=10,
      pady=5,
      sticky='ew'
    )
    self.MongoStatus.configure(state='disabled')

    self.openMongosh = ctk.CTkButton(
      self,
      text='Open MongoSH',
      command=lambda: MongoSH.startMongosh(self.client.conStr)
      )
    self.openMongosh.grid(
      row=4,
      column=0,
      padx=10,
      pady=5,
      sticky='ew'
      )
    
    self.launchCompassButton = ctk.CTkButton(
      self,
      text='Open Compass',
      command=lambda: Compass.startCompass(self.client.conStr)
      )
    self.launchCompassButton.grid(
      row=5,
      column=0,
      padx=10,
      pady=5,
      sticky='ew'
      )

    self.monitorMongoDB()

  def startMongoDB(self):
    self.client.StartService()
    self.monitorMongoDB()
  
  def stopMongoDB(self):
    self.client.StopService()
    self.monitorMongoDB()

  def monitorMongoDB(self):
    status = self.client.mongoStatus()
    if status == 'stopped':
      self.startMongo.configure(state='normal')
      self.MongoStatus.configure(
        text='MongoDB: Off',
        text_color_disabled='black',
        fg_color='grey',
      )
      self.stopMongo.configure(state='disabled')

    elif status == 'running':
      self.startMongo.configure(state='disabled')
      self.MongoStatus.configure(
        text='MongoDB: On',
        text_color_disabled='black',
        fg_color='green'
      )
      self.stopMongo.configure(state='normal')