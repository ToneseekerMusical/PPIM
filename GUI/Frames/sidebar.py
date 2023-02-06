import customtkinter, time
import Controllers.Mongo as Mongo
import Controllers.System as System

class SidebarFrame(customtkinter.CTkFrame):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
        # create sidebar frame with widgets

    self.logo_label = customtkinter.CTkLabel(
      self,
      text="PPIM",
      font=customtkinter.CTkFont(
        size=20,
        weight="bold"
        )
      )
    self.logo_label.grid(
      row=0,
      column=0,
      padx=20,
      pady=(20, 10))
    
    #management buttons

    self.startMongo = customtkinter.CTkButton(
      self,
      text='Start MongoDB',
      command=self.startMongoDB
      )
    self.startMongo.grid(
      row=2,
      column=0,
      padx=20,
      pady=10
      )

    self.stopMongo = customtkinter.CTkButton(
      self,
      text='Stop MongoDB',
      command=self.stopMongoDB
      )
    self.stopMongo.grid(
      row=3,
      column=0,
      padx=20,
      pady=10
      )

    self.MongoStatus = customtkinter.CTkLabel(
      self,
      text='MongoDB: Off',
      text_color='black',
      bg_color='grey',
      corner_radius=10,
    )
    self.MongoStatus.grid(
      row=4,
      column=0,
      padx=20,
      pady=10,
    )

    #updates and Settings
    self.options = customtkinter.CTkTabview(
      self,
      150,
    )
    self.options.grid(
      row=6,
      column=0,
    )
    self.options.add('updates')
    self.options.add('settings')
    self.options.tab('updates').grid_columnconfigure(0, weight=1)
    self.options.tab('settings').grid_columnconfigure(0, weight=1)

    #updates
    self.updateNodeButton = customtkinter.CTkButton(
      self.options.tab('updates'),
      text='Update Node Version',
      command=self.updateNode
    )
    self.updateNodeButton.grid(
      row=1,
      column=0,
      padx=20,
      pady=(10,0)
    )
    
    self.updateMongoDBButton = customtkinter.CTkButton(
      self.options.tab('updates'),
      text='Update MongoDB',
      command=self.UpdateMongoDB
    )
    self.updateMongoDBButton.grid(
      row=3,
      column=0,
      padx=20,
      pady=(10,0)
    )

#    self.progressbar_1 = customtkinter.CTkProgressBar(
#      self.options.tab('updates'),
#      )
#    self.progressbar_1.grid(
#      row=4,
#      column=0,
#      padx=(20, 10),
#      pady=(10, 10),
#      sticky="ew"
#      )
#
#    self.updateReadout = customtkinter.CTkLabel(
#      self.options.tab('updates'),
#      text="idealTree:projectName: sill idealTree buildDeps",
#      anchor="w"
#      )
#    self.updateReadout.grid(
#      row=5,
#      )

    #Settings
    self.settings = customtkinter.CTkButton(
      self.options.tab('settings'),
      text='Settings',
      command=self.openSettings
    )
    self.settings.grid(
      row=1,
      column=0,
      padx=20,
      pady=(10,0)
    )

    self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
      self.options.tab('settings'), 
      values=["Light", "Dark", "System"],
      command=self.change_appearance_mode_event
      )
    self.appearance_mode_optionemenu.grid(
      row=2,
      column=0,
      padx=20,
      pady=(10, 10)
      )

    self.scaling_label = customtkinter.CTkLabel(
      self.options.tab('settings'),
      text="UI Scaling:",
      anchor="w")
    self.scaling_label.grid(
      row=3,
      column=0,
      padx=20,
      pady=(10, 0)
      )

    self.scaling_optionemenu = customtkinter.CTkOptionMenu(
      self.options.tab('settings'),
      values=["80%", "90%", "100%", "110%", "120%"],
      command=self.change_scaling_event
      )
    self.scaling_optionemenu.grid(
      row=4,
      column=0,
      padx=20,
      pady=(10, 20)
      )

    # set default values
    #self.progressbar_1.configure(mode="indeterminnate")
    #
    #self.progressbar_1.start()
  
  def change_appearance_mode_event(self, new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)

  def change_scaling_event(self, new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)
  
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

  def updateNode(self):
    print("updateNode")

  def updatePackages(self):
    print("updatePackages")

  def UpdateMongoDB(self):
    print("UpdateMongoDB")

  def openSettings(self):
    print("openSettings")