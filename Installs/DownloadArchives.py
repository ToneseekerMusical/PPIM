# imported the requests library
from urllib.request import urlopen, urlretrieve
import json
import platform
import os

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
    return parseJson(url)['versions'][0]['platform']

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
        ver = MongoDBSelectEdition(ver,'base')
        ver = MongoDBOSSelect(ver,osVer['system'])
        url = ver['archive']['url']
        filename = url.split('/')[-1]
        return {'url': url, 'filename':filename}
    elif program.lower() in ('compass','mongosh'):
        ver = latestCompassAndShell(url)
        ver = CompassAndShellOSSelect(ver,osVer['system'])
        url = ver[0]['download_link']
        filename = url.split('/')[-1]
        if program.lower() != 'mongosh':
            filename = filename.split('-')[1:]
            filename = '-'.join(filename)
        return {'url': url, 'filename':filename}

def parseNodeJSURL(url):
    osVer = osVersion()
    ver = latestNodeJS(url)
    ver = architectureCheck(ver,osVer['arch'])
    #print(nodeVer)
    ver = NodeOSSelect(ver,osVer['system'])
    url = "https://nodejs.org/dist/" + ver['version'] + '/node-' + ver['version'] + '-' + ver['files'][0]
    return {'url':url,'filename':'node-' + ver['version'] + '-' + ver['files'][0]}

def parseVSCodeURL(url):
    url = urlopen(url)
    cd = url.info()['Content-Disposition']
    filename = cd.split('"')[1]
    return{'url':url,'filename':filename}

#Downloads the archives
def downloadMongoAndNode():
    downloadInfo = (
        parseMongoURL("mongodb","http://downloads.mongodb.org.s3.amazonaws.com/current.json"),
        parseMongoURL("compass","https://info-mongodb-com.s3.amazonaws.com/com-download-center/compass.json"),
        parseMongoURL("mongosh","https://s3.amazonaws.com/info-mongodb-com/com-download-center/mongosh.json"),
        parseNodeJSURL("https://nodejs.org/download/release/index.json"),
        parseVSCodeURL("https://update.code.visualstudio.com/latest/win32-x64-archive/stable")
        )
    for download in downloadInfo:
        if not os.path.exists('Installs/'+download['filename']):
            urlretrieve(download['url'],'Installs/'+download['filename'])
        else:
            print('Latest already downloaded')

downloadMongoAndNode()