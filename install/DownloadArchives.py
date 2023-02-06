from urllib.request import urlopen, urlretrieve
import json
import platform
import os
import pathlib

# Opens a JSON file and returns the json in a python readable format
def parseJson(url):
    response = urlopen(url)
    return json.loads(response.read())

# Gets CPU Architecture and Operating system version
def osVersion():
    _os_bit=64
    if os.environ.get('PROCESSOR_ARCHITECTURE').lower() == 'x86' and os.environ.get('PROCESSOR_ARCHITEW6432') is None: _os_bit=32
    return {'system': platform.system(), 'arch': _os_bit }

# Gets version info as json removes non LTS versions returning the filtered list
def latestMongoDB(url):
    versionList = parseJson(url)['versions']
    lts = list(filter(lambda ver: ver['lts_release'] == True, versionList))
    return lts[0]

def latestCompassAndShell(url):
    ver = parseJson(url)['versions'][0]
    version = ver['version']
    file = ver['platform']
    return {'file':file,'version':version}

def latestNodeJS(url):
    versionList = parseJson(url)
    lts = list(filter(lambda ver: ver['lts'] != False, versionList))[0]
    lts['files'] = [x for x in lts['files'] if 'zip' in x ]
    return lts

#Selects MongoDB Version
def MongoDBSelectEdition(ver, edition):
    return [x for x in ver['downloads'] if x['edition'] == edition]

#Matches OS Version to Targeted Version
def MongoDBOSSelect(ver, os:str):
    if os == 'Windows':
        return [x for x in ver if x['target'] == os.lower()][0]
    #add further logic for other operating systems

def CompassAndShellOSSelect(ver, os:str):
    if os == 'Windows':
        ver = [x for x in ver if os.lower() in x['name'].lower()]
        return [x for x in ver if 'zip' in x['download_link'].lower()]

def NodeOSSelect(nodeVer, os:str):
    if os == 'Windows':
        nodeVer['files'] = [x for x in nodeVer['files'] if 'win' in x ]
        nodeVer['files'] = [x for x in nodeVer['files'] if 'zip' in x ]
        nodeVer['files'][0] = nodeVer['files'][0][:-4]+'.zip'
    #add further logic for other operating systems
    return nodeVer

# Matches cpu architecture to NodeJS version
def architectureCheck(nodeVer, bit):
    if bit == 32:
        nodeVer['files'] = [x for x in nodeVer['files'] if 'x86' in x ]
    else:
        nodeVer['files'] = [x for x in nodeVer['files'] if 'x64' in x ]
    return nodeVer

def parseMongoURL(program:str, url):
  osVer = osVersion()
  if program.lower() == 'mongodb':
      ver = latestMongoDB(url)
      version = ver['version']
      ver = MongoDBSelectEdition(ver,'base')
      ver = MongoDBOSSelect(ver,osVer['system'])
      url = ver['archive']['url']
      filename = url.split('/')[-1]
      return {'url': url, 'filename':filename, 'version':version}
  elif program.lower() in ('compass','mongosh'):
      ver = latestCompassAndShell(url)
      version = ver['version']
      ver = CompassAndShellOSSelect(ver['file'],osVer['system'])
      url = ver[0]['download_link']
      filename = url.split('/')[-1]
      if program.lower() != 'mongosh':
          filename = filename.split('-')[1:]
          filename = '-'.join(filename)
      return {"url": url, "filename":filename, "version":version}

def parseNodeJSURL(url):
  osVer = osVersion()
  ver = latestNodeJS(url)
  version = ver['version']
  ver = architectureCheck(ver,osVer['arch'])
  ver = NodeOSSelect(ver,osVer['system'])
  url = "https://nodejs.org/dist/" + ver['version'] + '/node-' + ver['version'] + '-' + ver['files'][0]
  return {"url":url,"filename":'node-' + ver['version'] + '-' + ver['files'][0],"version":version}

def downloadVSCode(path):
  vscode_url = "https://update.code.visualstudio.com/latest/win32-x64-archive/stable"
  vscodeVer = urlopen(vscode_url)
  contentdisposition = vscodeVer.info()['Content-Disposition']
  filename = contentdisposition.split('"')[1].split('-')[0]+'.zip'
  version = contentdisposition.split('"')[1].split('-')[-1][:-4]
  if not os.path.exists(path+filename):
    urlretrieve(vscode_url, path+filename)
  else:
    print('LTS VS Code already downloaded')
  return version

#Downloads the archives
def downloadAll():
  path = pathlib.Path
  cwd = str(pathlib.Path.cwd())
  downloadInfo = {
    "MongoDB":parseMongoURL("mongodb","http://downloads.mongodb.org.s3.amazonaws.com/current.json"),
    "Compass":parseMongoURL("compass","https://info-mongodb-com.s3.amazonaws.com/com-download-center/compass.json"),
    "Mongosh":parseMongoURL("mongosh","https://s3.amazonaws.com/info-mongodb-com/com-download-center/mongosh.json"),
    "Node":parseNodeJSURL("https://nodejs.org/download/release/index.json"),
    }
  versions = {}
  for dependency, download in downloadInfo.items():
    versions[dependency] = download['version']
    if not path(cwd+'/lib/'+dependency).exists():
      if not path(cwd+'/tmp/'+dependency.lower()+'.zip').exists():
        if not path(cwd+'/tmp').exists():path(cwd+'/tmp').mkdir()
        urlretrieve(download['url'],cwd+'\\tmp\\'+dependency.lower()+'.zip')
        print(dependency + ' downloaded!')
      else:
        print('Latest already downloaded!')
  if not path(cwd+'/lib/VSCode').exists():
    versions['vscode'] = downloadVSCode(cwd+'\\tmp\\')
    print('VS Code downloaded!')
  return versions