import customtkinter as ctk
import Controllers.Mongo as Mongo

class mongoDBFrame(ctk.CTkFrame):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    #Create MongoDB Frame
    self.mongoDBlabel = ctk.CTkLabel(
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

    self.mongoDBURI = ctk.CTkLabel(
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

    self.mongoDBDatabase = ctk.CTkEntry(
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
      
    self.frontendTemplateLabel = ctk.CTkLabel(
      self,
      text="Frontend Template:",
      anchor="w"
      )
    self.frontendTemplateLabel.grid(
      row=2,
      column=0,
      padx=5,
      pady=5,
      sticky='w'
      )
    
    self.frontendTemplateSelect = ctk.CTkOptionMenu(
      self,
      values = ['Payload Website'],
      command=self.FrontendTemplate
    )
    self.frontendTemplateSelect.grid(
      row=2,
      column=1,
      padx=5,
      pady=5
    )
      
    self.backendTemplateLabel = ctk.CTkLabel(
      self,
      text="Frontend Template:",
      anchor="w"
      )
    self.backendTemplateLabel.grid(
      row=3,
      column=0,
      padx=5,
      pady=5,
      sticky='w'
      )
    
    self.backendTemplateSelect = ctk.CTkOptionMenu(
      self,
      values = ['Payload Admin'],
      command=self.BackendTemplate
    )
    self.backendTemplateSelect.grid(
      row=3,
      column=1,
      padx=5,
      pady=5
    )

  def FrontendTemplate(self):
    print('Open Frontend')

  def BackendTemplate(self):
    print('Open Frontend')