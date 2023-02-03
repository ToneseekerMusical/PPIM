import pathlib
import os
import re
import subprocess

def selectFile(file):
    path = pathlib.Path(__file__).parent.iterdir()
    dirs = list(filter(lambda path: path.is_dir(), path))
    mongoDir = [x for x in dirs if 'mongo' in x.name][0].iterdir()
    mongoBin = list(filter(lambda path: path.is_dir(), mongoDir))[0].iterdir()
    bin = [x for x in mongoBin if file in x.name.lower()]
    return bin

def checkPATH(path):
    env=os.getenv('PATH')
    env=env.split(';')
    env = [x for x in env if x != '']
    env = [sub.replace('WINDOWS', '%SystemRoot%') for sub in env]
    env = [(re.sub(r'(.*)\\Users\\(.*)\\AppData',"%USERPROFILE%\\\\AppData",x)) for x in env]


    if path in env:
        print('Path is already in environment')
    else:
        env.append(str(path).capitalize())
        env = ';'.join(env)
        envCMD = "[Environment]::SetEnvironmentVariable('PATH',"+env+"'Machine')"
        print(envCMD)
#        subprocess.Popen('powershell.exe')
        

def start(file):
    file = selectFile(file)[0]
    folder = file.parent
    checkPATH(folder)
    #os.chdir(str(folder))
    #os.system(file.name)

start('mongos.exe')

#Mongo('mongos.exe')
#Mongo('mongod.exe')

#file = selectFile('mongod.exe')[0]
#file = selectFile('mongos.exe')[0]