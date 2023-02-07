import customtkinter as ctk
import Controllers.Mongo as Mongo
import Controllers.System as System

class MongoFrame(ctk.CTkFrame):
  def __init__(self, *args, **kwargs):
    super().__init__(
      bg_color='transparent',
      fg_color='transparent',
      *args,
      **kwargs
      )
    
    self.grid_rowconfigure((0,1,2,3,4), weight=0)
    self.grid_rowconfigure(5, weight=1)
    
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
      padx=20,
      pady=(20, 10),
      sticky='nsew'
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
      padx=20,
      pady=10
      )

    self.stopMongo = ctk.CTkButton(
      self,
      text='Stop MongoDB',
      command=self.stopMongoDB
      )
    self.stopMongo.grid(
      row=2,
      column=0,
      padx=20,
      pady=10
      )

    self.MongoStatus = ctk.CTkLabel(
      self,
      text='MongoDB: Off',
      text_color='black',
      bg_color='grey',
      corner_radius=10,
    )
    self.MongoStatus.grid(
      row=3,
      column=0,
      padx=20,
      pady=10,
    )

    self.openMongosh = ctk.CTkButton(
      self,
      text='Open MongoSH',
      command=self.openMongoSH
      )
    self.openMongosh.grid(
      row=4,
      column=0,
      padx=20,
      pady=10
      )

    self.monitorMongoDB()

  def startMongoDB(self):
    Mongo.startDB()
    self.monitorMongoDB()
  
  def stopMongoDB(self):
    Mongo.stopDB()
    self.monitorMongoDB()

  def monitorMongoDB(self):
    status = System.mongoStatus()
    if status == 'stopped':
      self.startMongo.configure(state='normal')
      self.MongoStatus.configure(
        text='MongoDB: Off',
        text_color='black',
        bg_color='grey',
      )
      self.stopMongo.configure(state='disabled')

    elif status == 'running':
      self.startMongo.configure(state='disabled')
      self.MongoStatus.configure(
        text='MongoDB: On',
        text_color='black',
        bg_color='green'
      )
      self.stopMongo.configure(state='normal')

  def openMongoSH(self):
    print('Open Mongosh!')