import customtkinter as ctk

class pluginFrame(ctk.CTkTabview):
  def __init__(self, plugins, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      width=5,
      height=5,
      *args,
      **kwargs
      )
    
    self.add('Plugins')
    
    self.inputs = {}

    self.row = 0
    self.column = 0
    columnarray = ()

    for plugin in plugins:
      self.inputs[plugin] = ctk.CTkCheckBox(
        self.tab('Plugins'),text=f'{plugin.replace("-"," ")}',
        onvalue=True,offvalue=False)

    field:ctk.CTkBaseClass
    for field in self.inputs.values():
      field.grid(row=self.row,column=self.column,pady=5,padx=7,sticky='w')
      self.row += 1
      if self.row > 3:
        self.row = 0
        columnarray = columnarray + (self.column,)
        self.column += 1
    self.grid_columnconfigure(tuple(columnarray),weight=1)
