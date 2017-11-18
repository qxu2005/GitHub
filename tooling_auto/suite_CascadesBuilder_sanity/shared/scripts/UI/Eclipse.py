import sys
import squish
import test
import exceptions
import object
from Config import Config
import UI.windows.Preferences

def startIDE():
    ''' Launch QNX Momentics IDE '''
    if sys.platform == "darwin":
        squish.startApplication("Momentics")
    else:
        squish.startApplication("qde")
      
        

def setWorkspacePath(aPath):
    ''' Set path in workspace launcher '''
    squish.waitForObject(":Workspace Launcher_Shell", 60000)
    squish.type(squish.waitForObject(":Workspace Launcher.Workspace:_Combo"), aPath)
    squish.clickButton(squish.waitForObject(":Workspace Launcher.OK_Button"))
    squish.waitForObject(":C/C++ - Welcome - QNX Momentics IDE.Welcome_CTabItem",25000)
    
    window = squish.waitForObject(":C/C++ - QNX Momentics IDE_Shell")
    window.setMaximized(True)
    
    enabled = squish.waitFor('object.exists(":Authentication Required.OK_Button")',10000)
  
    if enabled:
        squish.clickButton(squish.waitForObject(":Authentication Required.OK_Button"))
        if object.exists(":Authentication Required.OK_Button"):
            squish.clickButton(squish.waitForObject(":Authentication Required.OK_Button"))
    
    
    CloseAll()
          
    squish.activateItem(squish.waitForObjectItem(":C/C++ - QNX Momentics IDE_Menu", "Window"))
    squish.activateItem(squish.waitForObjectItem(":Window_Menu", "Show Advanced Toolbars"))
    
    
    targetVersion =Config.getValue("TargetVersion", "version")
   
    if targetVersion is not None  and len(targetVersion) > 0 :
        try:
            UI.windows.Preferences.setNdkVersion(targetVersion)
        except exceptions.Exception, e:
            test.fatal("can not set target Version",str(e))
            raise

def exitIDE():
    ''' Exit IDE '''
    SaveAll()
    if sys.platform == "darwin":
        squish.nativeType("<Command+q>")
    else :
        squish.activateItem(squish.waitForObjectItem(":C/C++ - QNX Momentics IDE_Menu", "File"))
        squish.activateItem(squish.waitForObjectItem(":File_Menu", "Exit"))
        
    

def CloseAll():
    ''' Close all files '''
    if sys.platform == "darwin":
        squish.nativeType("<Command+Shift+w>")
    elif sys.platform =="linux2":
        squish.activateItem(squish.waitForObjectItem(":C/C++ - QNX Momentics IDE_Menu", "File"))
        squish.activateItem(squish.waitForObjectItem(":File_Menu", "Close All"))
    else :
        squish.nativeType("<Ctrl+Shift+w>")
            
            

def SaveAll():
    ''' save all  '''
    if sys.platform == "darwin":
        squish.nativeType("<Command+Shift+s>")
    else :
        squish.nativeType("<Ctrl+Shift+s>")
        
    

def InputKey(key):
    ''' enter key '''
    squish.nativeType(key)
        
        
    

def setFormat():
    ''' set file format '''
    if sys.platform == "darwin":
        squish.nativeType("<Command+Shift+f>")
    else :
        squish.nativeType("<Ctrl+Shift+f>")  
            
            
            

def setActiveProject(index =1):
    ''' set active project '''
    squish.snooze(2)
    squish.mouseClick(squish.waitForObject(":Projects_CListCombo"), 15, 15, 0, squish.Button.Button1)
    item = "{isvisible='true' occurrence='"+ str(index) +"' type='com.qnx.tools.utils.ui.controls.DefaultListItem' window=':_Shell'}"
    squish.mouseClick(squish.waitForObject(item), 15, 15, 0, squish.Button.Button1)


def launchDebug():
    ''' launch debug '''
    if sys.platform == "darwin":
        squish.nativeType("<Command+F11>")
    else :
        squish.nativeType("<F11>")
        


def stop():    
    ''' click stop tool item '''
    squish.mouseClick(squish.waitForObject(":Stop_ToolItem", 20000), 15, 15, 0, squish.Button.Button1)
        
        

def showExpressionView():
    ''' show expression view '''
    squish.activateItem(squish.waitForObjectItem(":C/C++ - QNX Momentics IDE_Menu", "Window"))
    squish.activateItem(squish.waitForObjectItem(":Window_Menu", "Show View"))
    squish.activateItem(squish.waitForObjectItem(":Show View_Menu", "Expressions"))  
    
        