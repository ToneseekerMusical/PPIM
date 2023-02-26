import ctypes
from pathlib import Path as Path
from Controllers.Mongo import MongoDB
from Controllers.System import System
from Controllers.Dependencies import Dependencies

class Setup():
  def __init__(self, phase:str, installPath="", mongoVer='base'):
    if phase.lower() not in ('install', 'config', 'add', 'check', 'update'): raise Exception('You must specify whether this is an installation or update.')
    self.__mongoVer = mongoVer
    self.__phase = phase
    
    if installPath != "":
      self.__instPath = Path(installPath)
    else:
      self.__instPath = Path.cwd()

  def Install(self):
    downloadDeps = Dependencies(self.__mongoVer,self.__phase,self.__instPath)
    mongoV = list(downloadDeps.allDependencies['MongoDB'].keys())[0]
    cfgPath = Path(f'{self.__instPath}\lib\MongoDB\{mongoV}\\bin\mongod.conf')

    srv = Path(f'{self.__instPath}\srv\mongodb')
    cfgTemplate = Path(f'{self.__instPath}\mongod.conf.template')

    cfgTemplate.touch()
    cfgTemplate.open('w')
    cfgTemplate.write_text("""
      # mongod.conf

      # for documentation of all options, see:
      #   http://docs.mongodb.org/manual/reference/configuration-options/

      # where to write logging data.
      systemLog:
        quiet: true
        traceAllExceptions: false
        path: <logpath>
        logAppend: true
        logRotate: rename
        destination: file

      # how the process runs
      processManagement:
        pidFilePath: <PIDPath>
        timeZoneInfo: <TzDBPath>

      # network interfaces
      net:
        port: 27017
        bindIp: 127.0.0.1, ::1, localhost
        ipv6: true

      # Where and how to store data.
      storage:
        dbPath: <storagepath>
    """)



    if not srv.is_dir(): srv.mkdir(parents=True)
    confc = open(cfgTemplate,'r').read()
    confc = confc.replace('<logpath>',f'{srv}\mongo.log')
    confc = confc.replace('<PIDPath>',f'{srv}\mongo.pid')
    confc = confc.replace('<TzDBPath>',f'{srv}')
    confc = confc.replace('<storagepath>',f'{srv}')

    Path(cfgPath).touch()
    conff = open(cfgPath,'w')
    conff.write(confc)
    conff.close()

    Path(f'{srv}\mongod.pid').touch()
    Path(f'{srv}\mongod.log').touch()
    if not Path(f'{self.__instPath}\websites').exists:
      Path(f'{self.__instPath}\websites').mkdir(parents=True)

    if not System().get_service('MongoDB'):
      ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",
        "powershell.exe",
        f"""
        mongod --config {cfgPath} --install --serviceName MongoDB;
        net start MongoDB
        """,
        None,
        0
      )
    
  def Config(self):
    dependencies = Dependencies(self.__mongoVer,'config',self.__instPath)
    dependencies = dependencies.allDependencies

    ver = '0.0.01dev'

    db = MongoDB()
    db.StartService()
    db.Connect(
    "mongodb://localhost:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=PPIM"
    )
    db = db.Connect(dbName='PPIM')
    sys = {
      'Version': ver,
      'Dependencies': dependencies
    }
    settings = {
      "_id": "Settings",
      "Accounts": {
        "Amazon-Web-Services": {"secretkey": "","publickey": ""},
        "Azure": {"secretkey": "","publickey": ""},
        "Cloudinary": {"secretkey": "","publickey": ""},
        "Github": {"username": "","password": ""},
        "Google-Clout-Storage": {"secretkey": "","publickey": ""},
        "Google-One-Tap": {"secretkey": "","publickey": ""},
        "Image-Kit": {"secretkey": "","publickey": ""},
        "Mongo-Atlas": {"username": "","password": ""},
        "Railways": {"username": "","password": ""},
        "S3": {"secretkey": "","publickey": ""},
        "Stripe": {"secretkey": "","publickey": ""},
        "Zapier": {"secretkey": "","publickey": ""}
        },
      "Directories": {
        "Project-Directory": {"directory": str(Path(f'{self.__instPath}\\websites\\'))},
        "NodeJS-Directory": {"directory": str(Path(f'{self.__instPath}\\lib\\NodeJS\\'))},
        "VSCode-Directory": {"directory": str(Path(f'{self.__instPath}\\lib\\VSCode\\'))},
        "MongoDB-Directory": {"directory": str(Path(f'{self.__instPath}\\lib\\MongoDB\\'))},
        "Mongosh-Directory": {"directory": str(Path(f'{self.__instPath}\\lib\\MongoSH\\'))},
        "Compass-Directory": {"directory": str(Path(f'{self.__instPath}\\lib\\Compass\\'))},
        "Github-Directory": {"directory": str(Path(f'{self.__instPath}\\lib\\Github\\'))},
        "DBTools-Directory": {"directory": str(Path(f'{self.__instPath}\\lib\\DBTools\\'))}
        },
      "MongoDB": {
        "Username": "",
        "Password": "",
        "DefaultHost": "",
        "DefaultPort": ""
        },
      "NodeJS": {
        "ScriptCommand": "NPM",
        "Dependencies": {},
        "Dev-Dependencies": {}
        },
      "Payload": {
        "defaultTemplate": "blank",
        "defaultAdminName": "",
        "defaultAdminPassword": "",
        'defaultPlugins':{
          "Auth0": False,"Blurhash": False,"Cloud-Storage": False,"Cloudinary": False,
          "Default-Roles": False,"Form-Builder": False,"Google-One-Tap": False,
          "Hash-Upload": False,"Image-Kit": False,"Lexical": False,"NestedDocs": False,
          "oAuth": False,"Phone-Field": False,"Redis-Cache": False,"S3-Upload": False,
          "Search": False,"SEO": False,"Stripe": False,"webP": False,"Zapier": False,
          "Redirects": False,"Base-64": False,"Password-Protection": False,
          "Resolve-Alias": False,"Tenancy": False
        }
      },
      "UI": {
        "appearance": "Light",
        "scaling": "80%"
      },
      "Updates": {
        "checkFrequency": "On Startup",
        "reminderFrequency": "On Startup",
        "bandwidthLimit": ""
      }
    }
    try:
      self.__system = db.create_collection('System',check_exists=True,capped=True,max=1,size=52428800)
      db.create_collection('Settings',check_exists=True,capped=True,max=1,size=52428800)
    except:
      self.__system = db.get_collection('System')
      self.__settings = db.get_collection('Settings')
      self.__system.insert_one(sys)
      self.__settings.insert_one(settings)