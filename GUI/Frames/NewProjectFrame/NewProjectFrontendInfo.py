import customtkinter as ctk

class frontendFrame(ctk.CTkTabview):
  def __init__(self, feTemplates, beTemplates, nodeVersions, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      width=5,
      height=5,
      *args,
      **kwargs
      )
    
    self.add('Frontend Config')

    self.labels = {
      'nodeVersion': ctk.CTkLabel(self.tab('Frontend Config'),text='NodeJS Version:'),
      'frontendTemplateLabel': ctk.CTkLabel(self.tab('Frontend Config'),text='Frontend Template:'),
      'adminTemplateLabel': ctk.CTkLabel(self.tab('Frontend Config'),text='Admin Template:'),
    }

    self.__rowcount = 0
    for label in self.labels:
      self.labels[label].grid(row = self.__rowcount,column=0,padx=5,pady=5,sticky='W')
      self.__rowcount += 1

    self.inputs = {
      'frontendTempSelect':ctk.CTkOptionMenu(self.tab('Frontend Config'),values=feTemplates),
      'adminTempSelect':ctk.CTkOptionMenu(self.tab('Frontend Config'),values=beTemplates),
      'nodeJSSelect':ctk.CTkOptionMenu(self.tab('Frontend Config'),values=nodeVersions)
    }

    self.__rowcount=0
    for field in self.inputs:
      self.inputs[field].grid(row=self.__rowcount,column=1,padx=5,pady=5,sticky='ew')
      self.__rowcount += 1