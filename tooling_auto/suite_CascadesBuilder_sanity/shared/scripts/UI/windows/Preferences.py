import squish
import object
from Wrapper.DropDownList import DropDownList
import sys



def disableQmlFolding():
    ''' disable QML header folding '''
    if sys.platform == "darwin":
        squish.nativeType("<Command+,>")
    else:
        squish.activateItem(squish.waitForObjectItem(":C/C++ - QNX Momentics IDE_Menu", "Window"))
        squish.activateItem(squish.waitForObjectItem(":Window_Menu", "Preferences"))
        
    squish.expand(squish.waitForObjectItem(":Preferences_Tree", "BlackBerry"))
    squish.expand(squish.waitForObjectItem(":Preferences_Tree", "QML Editor"))
    squish.mouseClick(squish.waitForObjectItem(":Preferences_Tree", "Folding"), 15, 15, 0, squish.Button.Button1)
    
    obj = squish.waitForObject(":Preferences.Header Comments_Button")
    if obj.selection == True:
        squish.clickButton(squish.waitForObject(":Preferences.Header Comments_Button"))
        squish.clickButton(squish.waitForObject(":Preferences.Apply_Button"))
    
    squish.clickButton(squish.waitForObject(":Preferences.OK_Button"))
    
    
    
def enableQmlDebug():
    ''' enable qml debug '''
    
    if sys.platform == "darwin":
        squish.nativeType("<Command+,>")
    else:
        squish.activateItem(squish.waitForObjectItem(":C/C++ - QNX Momentics IDE_Menu", "Window"))
        squish.activateItem(squish.waitForObjectItem(":Window_Menu", "Preferences"))
    
    
    squish.expand(squish.waitForObjectItem(":Preferences_Tree", "BlackBerry"))
    squish.mouseClick(squish.waitForObjectItem(":Preferences_Tree", "QML Debugging and Profiling"), 15, 15, 0, squish.Button.Button1)
    
    
    enabled = squish.waitFor('object.exists(":Preferences.Enable JavaScript Debugging_Button")',15000)
        
    if  enabled:
        obj = squish.waitForObject(":Preferences.Enable JavaScript Debugging_Button")
        if obj.selection == False:
            squish.clickButton(squish.waitForObject(":Preferences.Enable JavaScript Debugging_Button"))
            squish.clickButton(squish.waitForObject(":Preferences.Apply_Button"))
   
    squish.clickButton(squish.waitForObject(":Preferences.OK_Button"))
    
    
    

def disableMismatchCheck():
    ''' disable mismatch check ''' 
    if sys.platform == "darwin":
        squish.nativeType("<Command+,>")
    else:
        squish.activateItem(squish.waitForObjectItem(":C/C++ - QNX Momentics IDE_Menu", "Window"))
        squish.activateItem(squish.waitForObjectItem(":Window_Menu", "Preferences"))
        
    squish.expand(squish.waitForObjectItem(":Preferences_Tree", "BlackBerry"))
    squish.mouseClick(squish.waitForObjectItem(":Preferences_Tree", "Targets"), 15, 15, 0, squish.Button.Button1)
    squish.clickButton(squish.waitForObject(":Deployment.Ignore API Level mismatch when running an app (not recommended)_Button"))
    squish.clickButton(squish.waitForObject(":Deployment.Allow debugging and profiling with mismatched symbols (not recommended)_Button"))
    squish.clickButton(squish.waitForObject(":Preferences.OK_Button"))
       

    
    

def getNdkVersion():
    ''' get NDK version '''
    if sys.platform == "darwin":
        squish.nativeType("<Command+,>")
    else:
        squish.activateItem(squish.waitForObjectItem(":C/C++ - QNX Momentics IDE_Menu", "Window"))
        squish.activateItem(squish.waitForObjectItem(":Window_Menu", "Preferences"))
    
    squish.mouseClick(squish.waitForObjectItem(":Preferences_Tree", "QNX"), 15, 15, 0, squish.Button.Button1)
    info = squish.waitForObject(":Preferences.SDK_Version")
    ndkversion = info.getText()
    squish.clickButton(squish.waitForObject(":Preferences.OK_Button"))
    return ndkversion
        
        
        

def setNdkVersion(version):
    ''' set NDK version '''
    
    if sys.platform == "darwin":
        squish.nativeType("<Command+,>")
    else:
        squish.activateItem(squish.waitForObjectItem(":C/C++ - QNX Momentics IDE_Menu", "Window"))
        squish.activateItem(squish.waitForObjectItem(":Window_Menu", "Preferences"))
    squish.mouseClick(squish.waitForObjectItem(":Preferences_Tree", "QNX"), 15, 15, 0, squish.Button.Button1)
    combo = squish.waitForObject(":Preferences.SDK:_Combo")
    DropDownList.selectItem(combo,version)
    squish.clickButton(squish.waitForObject(":Preferences.OK_Button"))
        
       
        
        
         
        
    