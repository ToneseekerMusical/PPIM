import zipfile
import pathlib

def ExtractArchives(lib,filename:pathlib.Path,extraFolder=False):
  path = pathlib.Path
  with zipfile.ZipFile(str(filename), 'r') as zObject:
    if path(lib+filename.name[:-4]).exists():
      print('Files already extracted!')
    else:
      if extraFolder == False:
        zObject.extractall(str(path(lib)))
        l = path(lib).iterdir()
        l = list(filter(lambda x: filename.name[:-4] in str(x), l))[0]
        l.rename(lib+filename.name[:-4])
      else:
        zObject.extractall(str(path(lib+filename.name[:-4])))

def ExtractAllDependencies():
  path = pathlib.Path
  cwd = str(pathlib.Path.cwd())
  tmp = path(cwd+'/tmp/').iterdir()
  archives = list(filter(lambda x: 'zip' in str(x), tmp))
  for archive in archives:
    if 'vscode' in archive.name.lower():
      ExtractArchives(cwd+'\\lib\\',archive,True)
    elif 'compass' in archive.name.lower():
      ExtractArchives(cwd+'\\lib\\',archive,True)
    else:
      ExtractArchives(cwd+'\\lib\\',archive)

ExtractAllDependencies()