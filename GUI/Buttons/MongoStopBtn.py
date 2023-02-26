import customtkinter as ctk

class MongoStopBtn(ctk.CTkButton):
  def __ini__(self,*args,**kwargs):
    super().__init__(text='Start MongoDB',command=self.stopMongoDB,*args,*kwargs)

    self.grid(padx=5,pady=5,sticky='ew')

  def stopMongoDB(self):
    self.master.client.StopService()
    self.master.monitorMongoDB()