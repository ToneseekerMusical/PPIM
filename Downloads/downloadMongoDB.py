# imported the requests library
from urllib.request import urlopen, urlretrieve
import json
import platform
import os

mongoDB_JSON = "http://downloads.mongodb.org.s3.amazonaws.com/current.json"

# Opens a JSON file and returns the json in a python readable format
def parseJson(url):
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json

# Gets version info as json from mongodb.org, removes non LTS versions and
# executables returning the filtered list
def latestMongoDB(url):
    versionList = parseJson(url)['versions']
    lts = list(filter(lambda ver: ver['lts_release'] == True, versionList))
    lts = lts[0]
    return lts

def selectEdition(ver, edition):
    ver['downloads'] = [x for x in ver['downloads'] if x['edition'] == edition]
    return ver

# Gets CPU Architecture and Operating system version
def osVersion():
    _os_bit=64
    if os.environ.get('PROCESSOR_ARCHITECTURE').lower() == 'x86' and os.environ.get('PROCESSOR_ARCHITEW6432') is None: _os_bit=32
    return {'system': platform.system(), 'arch': _os_bit }

# Matches MongoDB version to OS
def osSelect(ver, os):
    if os == 'Windows':
        ver['downloads'] = [x for x in ver['downloads'] if x['target'] == os.lower()]
    #add further logic for other operating systems

    return ver

def MongoDBDownloadURL(url):
    osVer = osVersion()
    ver = latestMongoDB(url)
    ver = selectEdition(ver,'base')
    ver = osSelect(ver,osVer['system'])
    downloadURL = ver['downloads'][0]['archive']['url']
    return downloadURL

def downloadMongoDB(url):
    mongoDB = MongoDBDownloadURL(url)
    urlretrieve(mongoDB,'mongo.zip')

downloadMongoDB(mongoDB_JSON)