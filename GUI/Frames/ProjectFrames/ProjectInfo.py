import customtkinter as ctk

class projectInfo(ctk.CTkTabview):
  def __init__(self, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      width=5,
      height=5,
      *args,
      **kwargs)
    #create shell frame
    self.add('Site Info')
    self.add('Edit')

    self.tabs = {
      'Site Info':{
        'labels':{
          'frontendURLLabel':ctk.CTkLabel(self.tab('Site Info'),text='Frontend Link:',anchor='w'),
          'frontendCodeLabel':ctk.CTkLabel(self.tab('Site Info'),text='Frontend Code:',anchor='w'),
          'adminURLLabel':ctk.CTkLabel(self.tab('Site Info'),text='Admin Link:',anchor='w'),
          'adminCodeLabel':ctk.CTkLabel(self.tab('Site Info'),text='Admin Code:',anchor='w'),
          'nodeLabel':ctk.CTkLabel(self.tab('Site Info'),text='Node Version:',anchor='w'),
        },
        'inputs':{
          'FrontendURL': ctk.CTkLabel(self.tab('Site Info'),text='http://localhost:3001',anchor='w'),
          'AdminURL': ctk.CTkLabel(self.tab('Site Info'),text='http://localhost:3000',anchor='w'),
          'NodeVersion': ctk.CTkLabel(self.tab('Site Info'),text='v18.12.1',anchor='w'),
          'FrontendBtn': ctk.CTkButton(self.tab('Site Info'),text='Open in VS Code'),
          'AdminBtn': ctk.CTkButton(self.tab('Site Info'),text='Open in VS Code'),
        }
      },
      'Edit':{
        'labels':{
          'FrontendURLLabel': ctk.CTkLabel(self.tab('Edit'),text='Edit Frontend URL:',anchor='w'),
          'FrontendPortLabel': ctk.CTkLabel(self.tab('Edit'),text='Edit Frontend Port:',anchor='w'),
          'AdminURLLabel': ctk.CTkLabel(self.tab('Edit'),text='Edit Admin URL:',anchor='w'),
          'AdminPortLabel': ctk.CTkLabel(self.tab('Edit'),text='Edit Admin Port:',anchor='w'),
        },
        'inputs':{
          'FrontendURL':ctk.CTkEntry(self.tab('Edit'),placeholder_text='http://localhost'),
          'FrontendPort':ctk.CTkEntry(self.tab('Edit'),placeholder_text='3001'),
          'AdminURL':ctk.CTkEntry(self.tab('Edit'),placeholder_text='http://localhost'),
          'AdminPort':ctk.CTkEntry(self.tab('Edit'),placeholder_text='3000'),
          'Submit': ctk.CTkButton(self.tab('Edit'),text='Submit'),
        }
      }}

    row = 0
    column = 0
    for tab, groups in self.tabs.items():
      for group, fields in groups.items():
        for field in fields.keys():
          self.tabs[tab][group][field].grid(row=row,column=column,padx=5,pady=5,sticky='ew')
          row += 1
        row = 0
        column += 1
      row = 0
      column = 0

  def OpenFrontendCode(self):...
  def OpenAdminCode(self):...