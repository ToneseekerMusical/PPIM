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
      self.form[setting]['labels'] = {}
      self.form[setting]['inputs'] = {}
      self.form[setting]['labels']['account']=ctk.CTkLabel(self.form[setting]['frames'],text=f'{setting.replace("-"," ")}:', anchor='w')
      self.form[setting]['labels']['account'].grid(column=0,row=0,columnspan=2,sticky='ew')

      if setting in ('Github','Mongo-Atlas','Railways'):
        self.form[setting]['labels']['username']=ctk.CTkLabel(self.form[setting]['frames'],text='Username:',anchor='w')
        self.form[setting]['labels']['username'].grid(column=0,row=1,padx=(0,10),sticky='ew')

        self.form[setting]['labels']['password']=ctk.CTkLabel(self.form[setting]['frames'],text='Password:',anchor='w')
        self.form[setting]['labels']['password'].grid(column=0,row=2,padx=(0,10),sticky='ew')

        self.form[setting]['inputs']['username']=ctk.CTkEntry(self.form[setting]['frames'],placeholder_text='Username')
        self.form[setting]['inputs']['username'].grid(column=1,row=1,sticky='ew')

        self.form[setting]['inputs']['password']=ctk.CTkEntry(self.form[setting]['frames'],placeholder_text='Password')
        self.form[setting]['inputs']['password'].grid(column=1,row=2,sticky='ew')
      else:
        self.form[setting]['labels']['secretkey']=ctk.CTkLabel(self.form[setting]['frames'],text='Secret Key:',anchor='w')
        self.form[setting]['labels']['secretkey'].grid(column=0,row=1,padx=(0,10),sticky='ew')

        self.form[setting]['labels']['publickey']=ctk.CTkLabel(self.form[setting]['frames'],text='Public Key:',anchor='w')
        self.form[setting]['labels']['publickey'].grid(column=0,row=2,padx=(0,10),sticky='ew')

        self.form[setting]['inputs']['secretkey']=ctk.CTkEntry(self.form[setting]['frames'],placeholder_text='Secret Key')
        self.form[setting]['inputs']['secretkey'].grid(column=1,row=1,sticky='ew')

        self.form[setting]['inputs']['publickey']=ctk.CTkEntry(self.form[setting]['frames'],placeholder_text='Public Key')
        self.form[setting]['inputs']['publickey'].grid(column=1,row=2,sticky='ew')

      if column == 0:
        column += 1
      else:
        column -= 1
        row += 1