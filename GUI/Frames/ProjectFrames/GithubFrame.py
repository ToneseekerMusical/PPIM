import customtkinter as ctk

class GithubFrame(ctk.CTkTabview):
  def __init__(self, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      segmented_button_selected_color=('#979DA2', 'gray29'),
      segmented_button_selected_hover_color=('#979DA2', 'gray29'),
      width=5,
      height=5,
      *args,
      **kwargs)
    #create shell frame
    self.add('Github')
    self.tab('Github').grid_columnconfigure((0,1),weight=1)
    self.startFrontend = ctk.CTkButton(self.tab('Github'),text='Pull Frontend')
    self.startFrontend.grid(row=0,column=0,padx=5,pady=5,sticky='ew')
    self.pushFrontend = ctk.CTkButton(self.tab('Github'),text='Push Frontend')
    self.pushFrontend.grid(row=0,column=1,padx=5,pady=5,sticky='ew')
    self.startAdmin = ctk.CTkButton(self.tab('Github'),text='Pull Admin')
    self.startAdmin.grid(row=1,column=0,padx=5,pady=5,sticky='ew')
    self.pushAdmin = ctk.CTkButton(self.tab('Github'),text='Push Admin')
    self.pushAdmin.grid(row=1,column=1,padx=5,pady=5,sticky='ew')