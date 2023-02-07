import sys, os, traceback, psutil, ctypes


def mongoStatus():
    status = psutil.win_service_get('mongoDB').status()
    return status

def isUserAdmin():

  if os.name == 'nt':
    import ctypes
    # WARNING: requires Windows XP SP2 or higher!
    try:
      return ctypes.windll.shell32.IsUserAnAdmin()
    except:
      traceback.print_exc()
      print("Admin check failed, assuming not an admin.")
      return False
  elif os.name == 'posix':
    return os.getuid() == 0
    # Check for root on Posix
  else:
    raise(RuntimeError, "Unsupported operating system for this module: %s" % (os.name,))

def runAsAdmin(cmdLine=None, wait=True):

  if os.name != 'nt':
    raise(RuntimeError, "This function is only implemented on Windows.")

  import win32api, win32con, win32event, win32process
  from win32comext.shell.shell import ShellExecuteEx
  from win32comext.shell import shellcon

  python_exe = sys.executable

  if cmdLine is None:
    cmdLine = [python_exe] + sys.argv
  elif type(cmdLine) not in (tuple,list):
    raise( ValueError, "cmdLine is not a sequence.")
  cmd = '"%s"' % (cmdLine[0],)
  # XXX TODO: isn't there a function or something we can call to massage command line params?
  params = " ".join(['"%s"' % (x,) for x in cmdLine[1:]])
  cmdDir = ''
  #showCmd = win32con.SW_SHOWNORMAL
  showCmd = win32con.SW_HIDE
  lpVerb = 'runas'  # causes UAC elevation prompt.

  # print "Running", cmd, params

  # ShellExecute() doesn't seem to allow us to fetch the PID or handle
  # of the process, so we can't get anything useful from it. Therefore
  # the more complex ShellExecuteEx() must be used.

  # procHandle = win32api.ShellExecute(0, lpVerb, cmd, params, cmdDir, showCmd)

  procInfo = ShellExecuteEx(nShow=showCmd,
                            fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
                            lpVerb=lpVerb,
                            lpFile=cmd,
                            lpParameters=params)

  if wait:
    procHandle = procInfo['hProcess']    
    obj = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
    rc = win32process.GetExitCodeProcess(procHandle)
    #print "Process handle %s returned code %s" % (procHandle, rc)
  else:
    rc = None

  return rc

def test():
  rc = 0
  if not isUserAdmin():
    print("You're not an admin."), os.getpid(), "params: ", sys.argv
    #rc = runAsAdmin(["c:\\Windows\\notepad.exe"])
    rc = runAsAdmin()
  else:
    print("You are an admin!"), os.getpid(), "params: ", sys.argv
    rc = 0
  x = raw_input('Press Enter to exit.')
  return rc

def get_service(name):
  service = None
  try:
    service = psutil.win_service_get(name)
    service = service.as_dict()
  except:
    pass
  return service

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False