import customtkinter

class ShellFrame(customtkinter.CTkFrame):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    #create shell frame

    self.shelllabel = customtkinter.CTkLabel(self,text="Shell",)
    self.shelllabel.grid(row=0,column=0,padx=10,pady=5,sticky='w')

    self.shellDisplay = customtkinter.CTkTextbox(self,)
    self.shellDisplay.grid(row=1,column=0,columnspan=4,padx=5,pady=5,sticky="nsew",)

    self.entry = customtkinter.CTkEntry(self,placeholder_text="Type your command here")
    self.entry.grid(row=2,column=0,columnspan=3,padx=(5, 10),pady=(5, 5),sticky="nsew")

    self.commandSubmit = customtkinter.CTkButton(self,text='Submit',fg_color="transparent",border_width=2,text_color=("gray10", "#DCE4EE"),command=self.submitCommand)
    self.commandSubmit.grid(row=2,column=3,padx=(10, 5),pady=(5, 5),)

    #Default Configurations
    self.shellDisplay.insert("0.0", "Payload\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
  
  def submitCommand(self):
    print('submitCommand')