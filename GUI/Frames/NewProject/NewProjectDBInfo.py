import customtkinter
import Controllers

class mongoDBFrame(customtkinter.CTkFrame):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    #Create MongoDB Frame
    self.mongoDBlabel = customtkinter.CTkLabel(
      self,
      text="MongoDB Info",
      anchor="w"
      )
    self.mongoDBlabel.grid(
      row=0,
      column=0,
      padx=5,
      pady=5,
      sticky='w'
      )

    self.mongoDBURI = customtkinter.CTkLabel(
      self,
      text='mongodb://0.0.0.0:27017/'
      )
    self.mongoDBURI.grid(
      row=1,
      column=0,
      padx=5,
      pady=5,
      sticky='w'
      )

    self.mongoDBDatabase = customtkinter.CTkEntry(
      self,
      placeholder_text='Database Name'
      )
    self.mongoDBDatabase.grid(
      row=1,
      column=1,
      padx=(5,10),
      pady=5,
      sticky='ew'
      )
      
    self.mongoDBlabel = customtkinter.CTkLabel(
      self,
      text="Database Management",
      anchor="w"
      )
    self.mongoDBlabel.grid(
      row=2,
      column=0,
      padx=5,
      pady=5,
      sticky='w'
      )

    self.createDBName = customtkinter.CTkEntry(
      self,
      placeholder_text='Database Name'
      )
    self.createDBName.grid(
      row=3,
      column=0,
      padx=5,
      pady=5,
      sticky='ew'
      )

    self.createDatabaseButton = customtkinter.CTkButton(
      self,
      text='Create Database',
      command=self.createDatabase
      )
    self.createDatabaseButton.grid(
      row=3,
      column=1,
      padx=20,
      pady=5,
      sticky='e'
      )

    self.launchCompassButton = customtkinter.CTkButton(
      self,
      text='Open MongoDB Compass',
      command=MongoState.startCompass()
      )
    self.launchCompassButton.grid(
      row=4,
      column=0,
      columnspan=2,
      padx=20,
      pady=5,
      sticky='ew'
      )

  def createDatabase(self):
    print('createDatabase')

  def launchCompass(self):
    print('LaunchCompass')