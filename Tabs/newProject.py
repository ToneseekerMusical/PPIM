import customtkinter
from Frames.githubInfo import githubFrame
from Frames.mongoDBInfo import mongoDBFrame
from Frames.plugins import pluginFrame
from Frames.projectInfo import projectFrame
from Frames.shell import shellFrame

class newProject():
  def __init__(self,tabview:customtkinter.CTkTabview,tabname:str):
    super().__init__()
        # create tabview
    tabview.grid(
      row=0,
      column=1,
      sticky="nsew")
    tabview.add(tabname)
    tabview.tab(tabname).grid_columnconfigure((0,1,2), weight=1)  # configure grid of individual tabs
    tabview.tab(tabname).grid_rowconfigure(2, weight=1)  # configure grid of individual tabs

    #Create Project Frame
    self.projectInfo = projectFrame(tabview.tab(tabname),corner_radius=0)
    self.projectInfo.grid(
      row=0,
      column=0,
      sticky='nsew'
    )
    self.projectInfo.grid_columnconfigure((0,1), weight=1)

    #Create Github Frame
    self.github = githubFrame(tabview.tab(tabname),corner_radius=0,)
    self.github.grid(
      row=0,
      column=1,
      sticky='nsew'
    )
    self.github.grid_columnconfigure((0,1,2), weight=1)

    #Create MongoDB Frame
    self.mongoDB = mongoDBFrame(tabview.tab(tabname),corner_radius=0,)
    self.mongoDB.grid(
      row=0,
      column=2,
      sticky='ew'
    )
    self.mongoDB.grid_columnconfigure((0,1),weight=1)

    #Create Plugin Frame
    self.plugins = pluginFrame(tabview.tab(tabname), corner_radius=0)
    self.plugins.grid(
      row=1,
      column=0,
      columnspan=2,
      sticky='new',
    )
    self.plugins.grid_columnconfigure((0,1,2,3,4,5), weight=1)

    #Create Payload Instance Frame
    self.createInstance_frame = customtkinter.CTkFrame(
      tabview.tab(tabname),
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
    self.shell = shellFrame(tabview.tab(tabname), corner_radius=0)
    self.shell.grid(
      row=2,
      column=0,
      columnspan=3,
      sticky="nsew"
    )
    self.shell.grid_columnconfigure((0,1,2), weight = 1)
    self.shell.grid_rowconfigure(1,weight=1)

    # set default values
    self.newPayloadInstance.configure(state='disabled')
  
  def createNewPayloadSite(self):
    print("createNewPayloadSite")