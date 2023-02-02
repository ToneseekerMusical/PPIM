import customtkinter

class mongoDBFrame(customtkinter.CTk):
  def __init__(self, tab):
    super().__init__()
    #Create MongoDB Frame
    self.mongoDB_frame = customtkinter.CTkFrame(
      tab,
      corner_radius=0,
    )
    self.mongoDB_frame.grid(
      row=0,
      column=2,
      sticky='ew'
    )
    self.mongoDB_frame.grid_columnconfigure((0,1),weight=1)

    self.mongoDBlabel = customtkinter.CTkLabel(
      self.mongoDB_frame,
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
      self.mongoDB_frame,
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
      self.mongoDB_frame,
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
      self.mongoDB_frame,
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
      self.mongoDB_frame,
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
      self.mongoDB_frame,
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
      self.mongoDB_frame,
      text='Open MongoDB Compass',
      command=self.launchCompass
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