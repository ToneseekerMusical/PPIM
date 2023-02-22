import customtkinter as ctk

class pluginFrame(ctk.CTkTabview):
  def __init__(self, plugins, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      width=5,
      height=5,
      segmented_button_selected_color=('#979DA2', 'gray29'),
      segmented_button_selected_hover_color=('#979DA2', 'gray29'),
      *args,
      **kwargs
      )
    
    self.add('Plugins')

    self.inputs = {}

    self.row = 0
    self.column = 0

    for plugin in plugins:
      self.inputs[plugin] = ctk.CTkCheckBox(
        self.tab('Plugins'),text=f'{plugin.replace("-"," ")}',
        onvalue=True,offvalue=False)

    field:ctk.CTkBaseClass
    for field in self.inputs.values():
      field.grid(row=self.row,column=self.column,pady=5,padx=5,sticky='ew')
      self.column += 1
      if self.column > (len(self.inputs.values())//6):
        self.column = 0
        self.row += 1

    self.tab('Plugins').grid_columnconfigure((0,1,2,3,4),weight=1)
