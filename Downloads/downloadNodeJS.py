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

# Gets version info as json from Nodejs.org, removes non LTS versions and
# executables returning the filtered list
def latestNodeJS(url):
    versionList = parseJson(url)
    lts = list(filter(lambda ver: ver['lts'] != False, versionList))
    lts = lts[0]
    lts['files'] = [x for x in lts['files'] if 'exe' not in x ]
    lts['files'] = [x for x in lts['files'] if 'msi' not in x ]
    return lts

# Gets CPU Architecture and Operating system version
def osVersion():
    _os_bit=64
    if os.environ.get('PROCESSOR_ARCHITECTURE').lower() == 'x86' and os.environ.get('PROCESSOR_ARCHITEW6432') is None: _os_bit=32
    return {'system': platform.system(), 'arch': _os_bit }

# Matches cpu architecture to NodeJS version
def architectureCheck(nodeVer, bit):
    if bit == 32:
        nodeVer['files'] = [x for x in nodeVer['files'] if 'x64' not in x ]
    else:
        nodeVer['files'] = [x for x in nodeVer['files'] if 'x86' not in x ]

    return nodeVer

# Matchese Node binary to OS
def osSelect(nodeVer, os):
    if os == 'Windows':
        nodeVer['files'] = [x for x in nodeVer['files'] if 'win' in x ]
        nodeVer['files'] = [x for x in nodeVer['files'] if 'zip' in x ]
        nodeVer['files'][0] = nodeVer['files'][0][:-4]+'.zip'
    #add further logic for other operating systems

    return nodeVer

def nodeJSDownloadURL(url):
    osVer = osVersion()
    nodeVer = latestNodeJS(url)
    nodeVer = architectureCheck(nodeVer,osVer['arch'])
    nodeVer = osSelect(nodeVer,osVer['system'])
    nodeDownloadURL = "https://nodejs.org/dist/" + nodeVer['version'] + '/node-' + nodeVer['version'] + '-' + nodeVer['files'][0]
    nodeInfo = {'url':nodeDownloadURL,'filename':'node-' + nodeVer['version'] + '-' + nodeVer['files'][0]}
    return nodeInfo

def downloadNodeJS():
    nodeJSON = "https://nodejs.org/download/release/index.json"
    nodeInfo = nodeJSDownloadURL(nodeJSON)
    if not os.path.exists('Installs/'+nodeInfo['filename']):
        urlretrieve(nodeInfo['url'],'Installs/'+nodeInfo['filename'])
    else:
        print('LTS Node already Downloaded')
        
downloadNodeJS()