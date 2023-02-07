import json, platform, os
from urllib.request import urlopen, urlretrieve

class update():
  def __init__(
    self,
    dependency:str,
    *args,
    **kwargs
    ):
    self.osV = self.__osVersion()

  def __parseJson(self,url):
      response = urlopen(url)
      return json.loads(response.read())

  def __osVersion(self):
      _os_bit=64
      if os.environ.get('PROCESSOR_ARCHITECTURE').lower() == 'x86' and os.environ.get('PROCESSOR_ARCHITEW6432') is None: _os_bit=32
      return {'system': platform.system(), 'arch': _os_bit }
  
  def __download(self):...
  def __verifyDownload(self):...
  def __NodeJS(self):...
  def __Compass(self):...
  def __MongoDB(self):...
  def __MongoSH(self):...
  def __VSCode(self):...
  def __PayloadCMS(self):...
  def __GitHub(self):...