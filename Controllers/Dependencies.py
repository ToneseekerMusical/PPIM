import urllib.error, urllib.request, urllib.parse, zipfile, os, re, ctypes
from urllib.request import urlopen, urlretrieve
from pathlib import Path
from pymongo.collection import Collection

class Dependencies():
  def __init__(self, mongoVersion:str, operation:str, dir:str = '', sysInfo:Collection = None):
    if operation.lower() not in ('install', 'config'): raise Exception('You must specify whether this is an installation or update.')
    if mongoVersion.lower() not in ('base', 'enterprise', 'source', 'targeted'): raise Exception('You must specify the MongoDB Edition.')
    if operation.lower() in ('add', 'update'): raise Exception('You must specify a connection string')

    self.urls = {
      'Compass':"https://info-mongodb-com.s3.amazonaws.com/com-download-center/compass.json",
      'DBTools':"https://s3.amazonaws.com/downloads.mongodb.org/tools/db/release.json",
      'Github':"https://github.com/cli/cli/releases/latest",
      'MongoDB':"http://downloads.mongodb.org.s3.amazonaws.com/current.json",
      'MongoSH':"https://s3.amazonaws.com/info-mongodb-com/com-download-center/mongosh.json",
      'NodeJS':"https://nodejs.org/download/release/index.json",
      'VSCode':"https://update.code.visualstudio.com/latest/win32-x64-archive/stable",
    }
    
    self.__operation = operation.lower()
    self.__mongoE = mongoVersion.lower()
    self.__sysInfo = sysInfo
    self.__osVersion()
    if dir == '':
      self.__path = str(Path.cwd())
    else:
      self.__path = str(dir)
    self.__tmp = Path(self.__path+'\\tmp\\')
    self.__lib = Path(self.__path+'\\lib\\')

    if self.__operation == 'install':
      self.__getJson()
      self.__GetAllVersions()
      self.__GetInstallDependencies()
      self.__Download()
      self.__ExtractDownloads()
      self.__CheckPaths()
      self.__SetPaths()
      self.__EmptyTmp()

    if self.__operation == 'config':
      self.__getJson()
      self.__GetAllVersions()
      self.__GetInstallDependencies()
      self.__Download()
      self.__ExtractDownloads()
      self.__CheckPaths()

    if self.__operation == 'check':
      self.__getJson()
      self.__UpdateCheck()

#    if self.__operation == 'update':
#      self.__Download()
#      self.__ExtractDownloads()
#      self.__CheckPaths()
#      self.__SetPaths()
#      self.__EmptyTmp()

#    if self.__operation == 'add':
#      self.__Download()
#      self.__ExtractDownloads()
#      self.__EmptyTmp()

#    if self.__operation == 'activate':
#      self.__CheckPaths()
#      self.__SetPaths()

  # Gets CPU Architecture and Operating system version
  def __osVersion(self):
      import os, platform, sys
      _os_bit=64

      if os.name == 'nt':
        archiveType = 'zip'
      if os.name == 'nt' and sys.version_info[:2] < (2,7):
          system =  os.environ.get("PROCESSOR_ARCHITEW6432", 
                os.environ.get('PROCESSOR_ARCHITECTURE', ''))
      else:
          system = platform.machine()

      if os.environ.get('PROCESSOR_ARCHITECTURE').lower() == 'x86' and os.environ.get('PROCESSOR_ARCHITEW6432') is None: _os_bit=32
      self.__os = {'system': platform.system().lower()[:3], 'sysalt':platform.system().lower(), 'arch': str(_os_bit), 'cpu': system, 'package':archiveType}
  
  # Opens a JSON file and returns the json in a python readable format
  def __parseJson(self,url):
      import json
      response = urlopen(url)
      return json.loads(response.read())
  
  # Loops through all dependencies and gets the version json from their
  # websites
  def __getJson(self):
    self.__json = {}
    for dep, url in self.urls.items():
      if url:
        if dep not in ('VSCode', 'Github'):
          self.__json[dep] = self.__parseJson(url)

  # Loops through all dependencies in the Download object, requests the JSON file from the distributor's 
  # website, parses the JSON into a version able to be inserted into the database. Marks each version as
  # not downloaded and not installed, and sends it to the object
  def __GetAllVersions(self):
    self.allDependencies = {}
    for dep, url in self.urls.items():
      version = 'error'
      self.allDependencies[dep] = {}
      if dep == 'MongoDB':
        self.__json[dep] = list(filter(lambda ver: ver['lts_release'] == True, self.__json[dep]['versions']))
        for version in self.__json[dep]:
          ver = [x for x in version['downloads'] if 'target' in x.keys() and self.__os['system'].lower() in x['target'] and self.__mongoE == x['edition'].lower()]
          for v in ver:
            self.allDependencies[dep][version['version']] = v['archive']
            self.allDependencies[dep][version['version']]['version'] = version['version']
            self.allDependencies[dep][version['version']]['active'] = False
            self.allDependencies[dep][version['version']]['current'] = False
            self.allDependencies[dep][version['version']]['downloaded'] = False
            self.allDependencies[dep][version['version']]['installed'] = False
            self.allDependencies[dep][version['version']]['used'] = False
      
      if dep == 'MongoSH':
        for versions in self.__json[dep]['versions']:
          self.allDependencies[dep][versions['version']] = {}
          vers = [x for x in versions['platform'] if self.__os['system'].lower() in x['name'].lower() and self.__os['package'].lower() in x['download_link']]
          for v in vers:
            self.allDependencies[dep][versions['version']]['url'] = v['download_link']
            self.allDependencies[dep][versions['version']]['version'] = versions['version']
            self.allDependencies[dep][versions['version']]['active'] = False
            self.allDependencies[dep][versions['version']]['current'] = False
            self.allDependencies[dep][versions['version']]['downloaded'] = False
            self.allDependencies[dep][versions['version']]['installed'] = False
            self.allDependencies[dep][versions['version']]['used'] = False

      if dep == 'Compass':
        versions = list(filter(lambda ver: 'beta' not in ver['version'].lower() and 'readonly' not in ver['version'].lower() and 'isolated' not in ver['version'].lower() ,self.__json[dep]['versions']))
        for version in versions:
          self.allDependencies[dep][version['_id']] = {}
          vers = [x for x in version['platform'] if 
                  self.__os['system'].lower() in x['name'].lower() and
                  self.__os['package'].lower() in x['download_link'].lower()]
          for ver in vers:
            self.allDependencies[dep][version['_id']]['url'] = ver['download_link']
            self.allDependencies[dep][version['_id']]['version'] = version['_id']
            self.allDependencies[dep][version['_id']]['active'] = False
            self.allDependencies[dep][version['_id']]['current'] = False
            self.allDependencies[dep][version['_id']]['downloaded'] = False
            self.allDependencies[dep][version['_id']]['installed'] = False
            self.allDependencies[dep][version['_id']]['used'] = False
      
      if dep == 'DBTools':
        for version in self.__json[dep]['versions']:
          self.allDependencies[dep][version['version']] = {}
          vers = [x for x in version['downloads'] 
                  if self.__os['system'].lower() in x['name'].lower()]
          for ver in vers:
            self.allDependencies[dep][version['version']] = ver['archive']
            self.allDependencies[dep][version['version']]['version'] = version['version']
            self.allDependencies[dep][version['version']]['active'] = False
            self.allDependencies[dep][version['version']]['current'] = False
            self.allDependencies[dep][version['version']]['downloaded'] = False
            self.allDependencies[dep][version['version']]['installed'] = False
            self.allDependencies[dep][version['version']]['used'] = False

      if dep == 'NodeJS':
        self.__json[dep] = list(filter(lambda x: x['lts'] != False and x['security'] == True, self.__json[dep]))
        verFilter = []
        for version in self.__json[dep]:
          vers = [x for x in version['files'] if self.__os['system'] in x and self.__os['arch'] in x and self.__os['package'] in x]
          for ver in vers:
            if str(version['version'].split(".")[0]) not in verFilter:
              verFilter.append(str(version["version"].split(".")[0]))
              self.allDependencies[dep][version['version']] = {}
              self.allDependencies[dep][version['version']]['version'] = version['version']
              self.allDependencies[dep][version['version']]['url'] = f"https://nodejs.org/dist/{version['version']}/node-{version['version']}-{vers[0][:-4]}.{self.__os['package']}"
              self.allDependencies[dep][version['version']]['active'] = False
              self.allDependencies[dep][version['version']]['current'] = False
              self.allDependencies[dep][version['version']]['downloaded'] = False
              self.allDependencies[dep][version['version']]['installed'] = False
              self.allDependencies[dep][version['version']]['used'] = False
      
      if dep == 'VSCode':
        vscode = urlopen(url)
        contentdisposition = vscode.info()['Content-Disposition']
        version = contentdisposition.split('"')[1].split('-')[-1][:-4]
        self.allDependencies[dep][version] = {}
        self.allDependencies[dep][version]['url'] = self.urls['VSCode']
        self.allDependencies[dep][version]['version'] = version
        self.allDependencies[dep][version]['active'] = False
        self.allDependencies[dep][version]['current'] = False
        self.allDependencies[dep][version]['downloaded'] = False
        self.allDependencies[dep][version]['installed'] = False
        self.allDependencies[dep][version]['used'] = False

      if dep == 'Github':
        github = urllib.request.Request(url)
        try:
          github = urllib.request.urlopen(github)
        except urllib.error.HTTPError as e:
          if e.status != 307:
            raise
          redirect = urllib.parse.urljoin(url, e.headers['location'])
          github = urllib.request.urlopen(redirect)
        version = github.url.split('/')[-1]
        ghURL = f'{github.url.replace("tag","download")}/gh_{version[1:]}_{self.__os["sysalt"].lower()}_{self.__os["cpu"]}.{self.__os["package"]}'
        self.allDependencies[dep][version] = {}
        self.allDependencies[dep][version]['url'] = ghURL
        self.allDependencies[dep][version]['version'] = version
        self.allDependencies[dep][version]['active'] = False
        self.allDependencies[dep][version]['current'] = False
        self.allDependencies[dep][version]['downloaded'] = False
        self.allDependencies[dep][version]['installed'] = False
        self.allDependencies[dep][version]['used'] = False

  # Filters dependency json based on the most recent version and adds
  # the version to the list if it's not in the list
  def __GetInstallDependencies(self):
    for dep, versions in self.allDependencies.items():
      downloads = list(versions.values())[0]
      for version, verInfo in versions.items():
        if verInfo == downloads:
          self.allDependencies[dep][version]['active'] = True
          self.allDependencies[dep][version]['current'] = True
          self.allDependencies[dep][version]['downloaded'] = False
          self.allDependencies[dep][version]['installed'] = False
          self.allDependencies[dep][version]['used'] = True
      self.allDependencies[dep]['hasUpdate'] = False
      self.allDependencies[dep]['updateVer'] = version
    self.downloads = self.allDependencies

#  def __UpdateCheck(self):
#    for dep, url in self.urls.items():
#      version = 'error'
#      if dep == 'MongoDB':
#        version = list(filter(lambda ver: ver['lts_release'] == True, self.__json[dep]['versions']))[0]
#        version = [x for x in version['downloads'] if 'target' in x.keys() and self.__os['system'].lower() in x['target'] and self.mongoE == x['edition'].lower()][0]
#        if version['version'] not in self.updates[dep]:
#          self.updates[dep][version['version']] = version['archive']
#          self.updates[dep][version['version']]['active'] = True
#          self.updates[dep][version['version']]['current'] = True
#          self.updates[dep][version['version']]['downloaded'] = False
#          self.updates[dep][version['version']]['installed'] = False
#          self.updates[dep][version['version']]['used'] = True
#          self.updates[dep]['hasUpdate'] = True
#          self.updates[dep]['updateVer'] = version['version']
#
#      if dep == 'Compass':
#        version = list(filter(lambda ver: 'beta' not in ver['version'].lower() and 'readonly' not in ver['version'].lower() and 'isolated' not in ver['version'].lower() ,self.__json[dep]['versions']))[0]
#        ver = [x for x in version['platform'] if self.__os['system'].lower() in x['name'].lower() and self.__os['package'].lower() in x['download_link'].lower()]
#        if version['id'] not in self.updates[dep]:
#          self.updates[dep][version['_id']] = {}
#          self.updates[dep][version['_id']]['url'] = ver['download_link']
#          self.updates[dep]['hasUpdate'] = version['_id']
#
#      if dep == 'MongoSH':
#        version = self.__json[dep]['versions'][0]
#        ver = [x for x in version['platform'] if self.__os['system'].lower() in x['name'].lower() and self.__os['package'].lower() in x['download_link']][0]
#        if not Path(f'{self.__lib}\{dep}\{version["_id"]}').exists():
#          self.updates[dep] = {}
#          self.updates[dep][version['_id']] = {}
#          self.updates[dep][version['_id']]['url'] = ver['download_link']
#          self.updates[dep]['hasUpdate'] = version['_id']
#
#      if dep == 'DBTools':
#        version = self.__json[dep]['versions'][0]
#        ver = [x for x in version['downloads'] 
#                  if self.__os['system'].lower() in x['name'].lower()][0]
#        if not Path(f'{self.__lib}\{dep}\{version["version"]}').exists():
#          self.updates[dep] = {}
#          self.updates[dep][version['version']] = ver['archive']
#          self.updates[dep]['hasUpdate'] = version['version']
#
#      if dep == 'NodeJS':
#        version = list(filter(lambda x: x['lts'] != False and x['security'] == True, self.__json[dep]))[0]
#        vers = [x for x in version['files'] if self.__os['system'] in x and self.__os['arch'] in x and self.__os['package'] in x]
#        if not Path(f'{self.__lib}\{dep}\{version["version"]}').exists():
#          self.updates[dep] = {}
#          self.updates[dep][version['version']] = {}
#          self.updates[dep][version['version']]['url'] = f"https://nodejs.org/dist/{version['version']}/node-{version['version']}-{vers[0][:-4]}.{self.__os['package']}"
#          self.updates[dep]['hasUpdate'] = version['version']
#
#      if dep == 'VSCode':
#        vscode = urlopen(url)
#        contentdisposition = vscode.info()['Content-Disposition']
#        version = contentdisposition.split('"')[1].split('-')[-1][:-4]
#        if not Path(f'{self.__lib}\{dep}\{version}').exists():
#          self.updates[dep] = {}
#          self.updates[dep][version] = {}
#          self.updates[dep][version]['url'] = self.urls['VSCode']
#          self.updates[dep]['hasUpdate'] = [version]
#
#      if dep == 'Github':
#        github = urllib.request.Request(url)
#        try:
#          github = urllib.request.urlopen(github)
#        except urllib.error.HTTPError as e:
#          if e.status != 307:
#            raise
#          redirect = urllib.parse.urljoin(url, e.headers['location'])
#          github = urllib.request.urlopen(redirect)
#        version = github.url.split('/')[-1]
#        ghURL = f'{github.url.replace("tag","download")}/gh_{version[1:]}_{self.__os["sysalt"].lower()}_{self.__os["cpu"]}.{self.__os["package"]}'
#        if not Path(f'{self.__lib}\{dep}\{version}').exists():
#          self.updates[dep] = {}
#          self.updates[dep]['hasUpdate'] = version
#          self.updates[dep][version] = {}
#          self.updates[dep][version]['url'] = ghURL

  def __Download(self):
    if not self.__tmp.exists():self.__tmp.mkdir()
    for dep, depInfo in self.downloads.items():
      versions = [x for x in depInfo.values() if type(x) == dict and x['used'] == True and x['downloaded'] == False and x['installed'] == False]
      for version in versions:
        if not Path(f'{self.__lib}\{dep}\{version["version"]}').exists():
          print(f'Downloading {dep} {version["version"]}')
          urlretrieve(version['url'],f'{self.__tmp}\{dep}-{version["version"]}.{self.__os["package"]}')
          self.downloads[dep][version['version']]['downloaded']=True
          self.downloads[dep][version['version']]['archivePath']=f'{self.__tmp}\{dep}-{version["version"]}.{self.__os["package"]}'
          print(f'Downloaded {dep} {version["version"]}')
        else:
          self.downloads[dep][version['version']]['downloaded']=True
          self.downloads[dep][version['version']]['archivePath']=f'{self.__tmp}\{dep}-{version["version"]}.{self.__os["package"]}'

  def __ExtractDownloads(self):
    for dep, depInfo in self.downloads.items():
      versions = [x for x in depInfo.values() if type(x) == dict and x['downloaded'] == True and 'PATH' not in x]
      for version in versions:
        print(f'Extracting {dep} {version["version"]}')
        src = f'{self.__tmp}\{dep}-{version["version"]}.{self.__os["package"]}'
        if dep in ('VSCode', 'Compass','Github'):
          dest = f'{self.__lib}\{dep}\{version["version"]}'
        else:
          dest = f'{self.__lib}\{dep}'
        try:
          with zipfile.ZipFile(src,'r') as zObject:
            if not Path(dest).exists(): Path(dest).mkdir(parents=True)
            zObject.extractall(dest)
            if dep in ('MongoDB', 'Github', 'MongoSH','DBTools','NodeJS'):
              for f in Path(f'{dest}\\').iterdir():
                  if version['version'].lower() in f.name:
                    f.rename(f'{dest}\{version["version"]}')
          self.downloads[dep][version['version']]['extracted'] = True
          if dep in ('Github', 'MongoDB','MongoSH','DBTools'):
            self.downloads[dep][version['version']]['PATH'] = f'{dest}\{version["version"]}\\bin\\'
          elif dep == 'NodeJS':
            self.downloads[dep][version['version']]['PATH'] = f'{dest}\{version["version"]}\\'
          else:
            self.downloads[dep][version['version']]['PATH'] = f'{dest}\\'
        except:
          self.downloads[dep][version['version']]['extracted'] = True
          if dep in ('Github', 'MongoDB','MongoSH','DBTools'):
            self.downloads[dep][version['version']]['PATH'] = f'{dest}\{version["version"]}\\bin\\'
          elif dep == 'NodeJS':
            self.downloads[dep][version['version']]['PATH'] = f'{dest}\{version["version"]}\\'
          else:
            self.downloads[dep][version['version']]['PATH'] = f'{dest}\\'

  def __CheckPaths(self):
    self.__env = str(os.getenv('Path')).split(';')
    self.__env = [x for x in self.__env if x != '']
    for dep, depInfo in self.downloads.items():
      instpath = Path(f'{str(self.__path)}/lib/{dep}')
      self.__env = [x for x in self.__env if str(instpath) not in x]
      versions = [x for x in depInfo.values() if type(x) == dict and 'PATH' in x and x['extracted'] == True and x['active'] == True]
      for version in versions:
        if version['used'] == True:
          if version['PATH'] not in self.__env:
            self.__env.append(version['PATH'])
            self.downloads[dep][version['version']]['installed'] = True
          else:
            self.downloads[dep][version['version']]['installed'] = True

  def __SetPaths(self):
    #Replace absolute Paths prefixes with wildcards
    self.__env = [sub.replace('C:\WINDOWS', '%SystemRoot%') for sub in self.__env]
    self.__env = [(re.sub(r'(.*)\\Users\\(.*)\\AppData',"%USERPROFILE%\\\\AppData",x)) for x in self.__env]
    self.__env = sorted([*set(self.__env)])
    self.__env = ';'.join(self.__env)
    var = "Path"
    scope = "Machine"

    commands = u"[Environment]::SetEnvironmentVariable('"+var+"','"+self.__env+"','"+scope+"')"
    
    ctypes.windll.shell32.ShellExecuteW(
      None,
      u"runas",
      u"powershell.exe",
      commands,
      None,
      1
    )

  def __EmptyTmp(self):
    for file in self.__tmp.iterdir():
        os.remove(file)