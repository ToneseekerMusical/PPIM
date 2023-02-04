from zipfile import ZipFile
import os

def ExtractArchives(path,filename,extraFolder=False):
  with ZipFile(path + '\\' + filename + '.zip', 'r') as zObject:
    if os.path.isdir(path+'\\'+filename):
      print('Files already exist!')
    else:
      if extraFolder == False:
        zObject.extractall(path=path)
      else:
        zObject.extractall(path=path + '\\' + filename)

def ExtractAllDependencies():
  path = os.path.dirname(__file__)
  files = os.listdir(path)
  files = [x for x in files if '.zip' in x ]
  for file in files:
    if 'vscode' in file.lower():
      ExtractArchives(path,file[:-4],True)
    elif 'compass' in file.lower():
      ExtractArchives(path,file[:-4],True)
    else:
      ExtractArchives(path,file[:-4])

ExtractAllDependencies()