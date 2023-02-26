import customtkinter as ctk

class MongoStartBtn(ctk.CTkButton):
  def __ini__(self,*args,**kwargs):
    super().__init__(text='Start MongoDB',command=self.startMongoDB,*args,*kwargs)

    self.grid(padx=5,pady=5,sticky='ew')

  def startMongoDB(self):
    self.master.client.StartService()
    self.master.monitorMongoDB()