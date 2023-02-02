import customtkinter
from Frames.githubInfo import githubFrame
from Frames.mongoDBInfo import mongoDBFrame
from Frames.plugins import pluginFrame
from Frames.projectInfo import projectFrame
from Frames.shell import shellFrame

class tabView(customtkinter.CTk):
  def __init__(self,window):
    super().__init__()
        # create tabview
    self.tabview = customtkinter.CTkTabview(window)
    self.tabview.grid(
      row=0,
      column=1,
      sticky="nsew")
    self.tabview.add(" + ")
    self.tabview.tab(" + ").grid_columnconfigure((0,1,2), weight=1)  # configure grid of individual tabs
    self.tabview.tab(" + ").grid_rowconfigure(2, weight=1)  # configure grid of individual tabs

    #Create Project Frame
    self.projectInfo = projectFrame(self.tabview.tab(' + '))

    #Create Github Frame
    self.github = githubFrame(self.tabview.tab(' + '))

    #Create MongoDB Frame
    self.mongoDB = mongoDBFrame(self.tabview.tab(' + '))

    #Create Plugin Frame
    self.plugins = pluginFrame(self.tabview.tab(' + '))

    #Create Payload Instance Frame
    self.createInstance_frame = customtkinter.CTkFrame(
      self.tabview.tab(' + '),
      corner_radius=0
    )
    self.createInstance_frame.grid(
      row=1,
      column=2,
      sticky='nsew',
    )

    self.createInstance_frame.grid_columnconfigure(0, weight=1)
    self.createInstance_frame.grid_rowconfigure(0, weight=1)
    self.newPayloadInstance = customtkinter.CTkButton(
      self.createInstance_frame,
      text='Create New Project',
      command=self.createNewPayloadSite
      )
    self.newPayloadInstance.grid(
      row=0,
      column=0,
      padx=20,
      pady=10,
      sticky='nsew'
      )

    #Create Shell Frame
    self.shell = shellFrame(self.tabview.tab(' + '))

    # set default values
    self.newPayloadInstance.configure(state='disabled')
  
  def createNewPayloadSite(self):
    print("createNewPayloadSite")