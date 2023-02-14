import customtkinter as ctk

class pluginSettings(ctk.CTkToplevel):
  def __init__(self, pluginName:str, *args, **kwargs):
    super().__init__(
      *args, **kwargs)

    self.pluginName = pluginName
    self._current_height = 500
    #sh = self.winfo_screenheight()//2
    #sw = self.winfo_screenwidth()//2
    self.grab_set()
    self.wm_title(f'{self.pluginName.replace("-"," ")} Settings')
    self.transient()
    self.resizable(False,False)
    self.update()
    self.inputs = {'test1':'','test2':'','test3':'','test4':'','test5':'','test6':'','test7':'','test8':''}
    for name, field in self.inputs.items():
      self.inputs[name] = ctk.CTkButton(self,text=name,width=350)
      self.inputs[name].pack(padx=10,pady=10)
    self.update()
    #wh = self.winfo_height()//2
    #ww = self.winfo_width()//2
    #self.geometry(f"{sw-ww}+{sh-wh}")

    # create label on CTkToplevel window
    #label = ctk.CTkLabel(self, text=self.pluginName)
    #label.pack(side="top", fill="both", expand=True, padx=20, pady=20)