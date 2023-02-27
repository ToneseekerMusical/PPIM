import customtkinter as ctk

class NewFrontendFrame(ctk.CTkTabview):
  def __init__(self, nodeversions:list, payloadversions:list, frontendTemplates:list, adminTemplates:list, *args, **kwargs):
    super().__init__(
      corner_radius=10,
      width=5,
      height=5,
      segmented_button_selected_color=('#979DA2', 'gray29'),
      segmented_button_selected_hover_color=('#979DA2', 'gray29'),
      *args,
      **kwargs
      )
    
    self.add('Frontend Config')

    self.tab('Frontend Config').grid_columnconfigure((0,1), weight=1)

    self.tabs = {
      'frontendConfig':{
        'labels':{
          'nodeVersionLabel': ctk.CTkLabel(self.tab('Frontend Config'),text='NodeJS Version:',anchor='w'),
          'PayloadVersionLabel': ctk.CTkLabel(self.tab('Frontend Config'),text='Payload Version:',anchor='w'),
          'frontendTemplateLabel': ctk.CTkLabel(self.tab('Frontend Config'),text='Frontend Template:',anchor='w'),
          'adminTemplateLabel': ctk.CTkLabel(self.tab('Frontend Config'),text='Admin Template:',anchor='w'),
        },
        'inputs':{
          'nodeJSversion':ctk.CTkOptionMenu(self.tab('Frontend Config'),values=nodeversions),
          'payloadVersion':ctk.CTkOptionMenu(self.tab('Frontend Config'),values=payloadversions),
          'frontendTemplate':ctk.CTkOptionMenu(self.tab('Frontend Config'),values=frontendTemplates),
          'adminTemplate':ctk.CTkOptionMenu(self.tab('Frontend Config'),values=adminTemplates),
          'frontendPort':ctk.CTkEntry(self.tab('Frontend Config'),placeholder_text='Frontend Port: 3001'),
          'adminPort':ctk.CTkEntry(self.tab('Frontend Config'),placeholder_text='Admin Port: 3000')
        }
      }
    }

    row = 0
    column = 0

    for tab, groups in self.tabs.items():
      for group, fields in groups.items():
        for field in fields.keys():
          padx=5
          if tab == 'backendConfig' and group == 'labels':
            padx = (5,24)
          self.tabs[tab][group][field].grid(row=row,column=column,padx=padx,pady=5,sticky='ew')
          row += 1
          if field == 'adminTemplate':
            column = 0
          if field == 'frontendPort':
            row -= 1
            column = 1
        row = 0
        column += 1
      column = 0
      row = 0

    