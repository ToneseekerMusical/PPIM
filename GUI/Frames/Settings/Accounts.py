import customtkinter as ctk

class Accounts(ctk.CTkFrame):
  def __init__(self,*args,**kwargs):
    super().__init__(
      fg_color='transparent',
      bg_color='transparent',
      *args,**kwargs)
    self.form = {
      'Amazon-Web-Services':{},
      'Azure':{},
      'Cloudinary':{},
      'Github':{},
      'Google-Clout-Storage':{},
      'Google-One-Tap':{},
      'Image-Kit':{},
      'Mongo-Atlas':{},
      'Railways':{},
      'S3':{},
      'Stripe':{},
      'Zapier':{},
    }

    self.grid_columnconfigure(0, weight=1)
    row = 0
    column = 0
    for setting in self.form.keys():
      self.form[setting]['frames']=ctk.CTkFrame(self,bg_color='transparent',fg_color='transparent')
      self.form[setting]['frames'].grid( row=row, column=column, pady=5, padx=5, sticky='ew')
      self.form[setting]['frames'].grid_columnconfigure(0,weight=1)

      self.form[setting]['labels']=ctk.CTkLabel(self.form[setting]['frames'],text=f'{setting.replace("-"," ")}:', anchor='w')
      self.form[setting]['labels'].grid(column=0,row=0,columnspan=2,sticky='ew')

      if setting in ('Github','Mongo-Atlas','Railways'):
        self.form[setting]['labels']=ctk.CTkLabel(self.form[setting]['frames'],text='Username:',anchor='w')
        self.form[setting]['labels'].grid(column=0,row=1,padx=(0,10),sticky='ew')

        self.form[setting]['labels']=ctk.CTkLabel(self.form[setting]['frames'],text='Password:',anchor='w')
        self.form[setting]['labels'].grid(column=0,row=2,padx=(0,10),sticky='ew')

        self.form[setting]['inputs']=ctk.CTkEntry(self.form[setting]['frames'],placeholder_text='Username')
        self.form[setting]['inputs'].grid(column=1,row=1,sticky='ew')

        self.form[setting]['inputs']=ctk.CTkEntry(self.form[setting]['frames'],placeholder_text='Password')
        self.form[setting]['inputs'].grid(column=1,row=2,sticky='ew')
      else:
        self.form[setting]['labels']=ctk.CTkLabel(self.form[setting]['frames'],text='Secret Key:',anchor='w')
        self.form[setting]['labels'].grid(column=0,row=1,padx=(0,10),sticky='ew')

        self.form[setting]['labels']=ctk.CTkLabel(self.form[setting]['frames'],text='Public Key:',anchor='w')
        self.form[setting]['labels'].grid(column=0,row=2,padx=(0,10),sticky='ew')

        self.form[setting]['inputs']=ctk.CTkEntry(self.form[setting]['frames'],placeholder_text='Secret Key')
        self.form[setting]['inputs'].grid(column=1,row=1,sticky='ew')

        self.form[setting]['inputs']=ctk.CTkEntry(self.form[setting]['frames'],placeholder_text='Public Key')
        self.form[setting]['inputs'].grid(column=1,row=2,sticky='ew')

      if column == 0:
        column += 1
      else:
        column -= 1
        row += 1