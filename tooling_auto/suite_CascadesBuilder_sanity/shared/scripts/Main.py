from Context import Context
from Config import Config
from BaseTools import BaseTools
import sys,os
import squish

import UI.Eclipse
import UI.view.SystemInfoPerspective 
import UI.windows.Target

import UI.windows.DeviceManager
import UI.windows.Perspective
import UI.view.SystemInfoPerspective


def init(filepath):
    """
    @summary:  initial Context and Config class
    @param filepath: the system file path 
    """
    Context.init(filepath)
    Config.init()
    
    squish.testSettings.logScreenshotOnError = True
    squish.testSettings.logScreenshotOnFail = True
    
    
def cleanUp(workspace=None):
    """
    @summary: delete workspace folder  and kill  AUT
    @param workspace: workspace to be deleted
    
    """
    if sys.platform == "darwin":
        BaseTools.killProcessByName("Momentics")
    elif sys.platform == "win32":
        BaseTools.killProcessByName("qde.exe")
    else:
        BaseTools.killProcessByName("qde")
    if workspace is None:  
        BaseTools.deleteFolder(__getWorkSpace())
    else:
        BaseTools.deleteFolder(workspace)
    
    
def __getWorkSpace():
    """
    @summary: get default workspace
    """
    return os.path.join(os.path.expanduser("~"),'testfolder')
    
    
def startUp(workspace=None):
    """
    @summary: start AUT
    """
    UI.Eclipse.startIDE()
    if workspace is None:
        UI.Eclipse.setWorkspacePath(__getWorkSpace())
    else:
         UI.Eclipse.setWorkspacePath(workspace)
  
    
    
def quit():
    """
    @summary:  quite AUT
    """
    UI.Eclipse.exitIDE()
    
    
def createTarget(debugtoken=True):
    """
    @summary:  create a new blackberry Target
    @param debugtoken:  create/upload debug token if True
    
    """
        
    UI.windows.Perspective.openSysInfoPerspective()
  
    UI.view.SystemInfoPerspective.delExistingDevice()

    UI.windows.Target.createBBTarget()
    
    UI.windows.Perspective.openCPerspective()
    
    if Context.GetContext('DEVICE') != 'NONE':
        UI.windows.Perspective.openSysInfoPerspective()
           
        UI.view.SystemInfoPerspective.killTestProcess()
    
        UI.windows.Perspective.openCPerspective()
   
        if debugtoken and  Context.GetContext('DEVICE') =='USB' :
            UI.windows.DeviceManager.createDebugToken()