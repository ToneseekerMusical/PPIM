# imported the requests library
from urllib.request import urlopen, urlretrieve
import json
import platform
import os

# Opens a JSON file and returns the json in a python readable format
def parseJson(url):
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json

# Gets version info as json from mongodb.org, removes non LTS versions and
# executables returning the filtered list
def latestMongoSH(url):
    versionList = parseJson(url)['versions'][0]['platform']
    return versionList

# Gets CPU Architecture and Operating system version
def osVersion():
    _os_bit=64
    if os.environ.get('PROCESSOR_ARCHITECTURE').lower() == 'x86' and os.environ.get('PROCESSOR_ARCHITEW6432') is None: _os_bit=32
    return {'system': platform.system(), 'arch': _os_bit }

# Matches MongoDB version to OS
def osSelect(ver, os):
    if os == 'Windows':
        ver = [x for x in ver if os.lower() in x['name'].lower()]
        ver = [x for x in ver if 'zip' in x['download_link'].lower()]
    return ver

def MongoSHDownloadURL(url):
    osVer = osVersion()
    ver = latestMongoSH(url)
    ver = osSelect(ver,osVer['system'])
    downloadURL = ver[0]['download_link']
    filename = downloadURL.split('/')[-1]
    mongoInfo = {'url': downloadURL, 'filename':filename}
    return mongoInfo

def downloadMongoSH():
    mongoJSON = "https://s3.amazonaws.com/info-mongodb-com/com-download-center/mongosh.json"
    mongoInfo = MongoSHDownloadURL(mongoJSON)
    if not os.path.exists('Installs/'+mongoInfo['filename']):
        urlretrieve(mongoInfo['url'],'Installs/'+mongoInfo['filename'])
    else:
        print('Latest MongoSH already downloaded')

downloadMongoSH()