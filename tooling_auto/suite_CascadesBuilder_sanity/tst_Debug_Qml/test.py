"""
@summary:Test  QML File  Debug

"""


import imp
imp.load_source("None", findFile("scripts", "AddPath.py"))

import os,sys,platform
import Main
import Project
import UI.view.QmlEditor
import Debug
import UI.windows.Preferences

from BaseTools import  BaseTools



def main(projectname=None):

    Main.init(os.path.realpath(__file__))
    
    Main.cleanUp()
    
    Main.startUp()
    
    Main.createTarget()
   
   
    UI.windows.Preferences.disableQmlFolding()
    UI.windows.Preferences.enableQmlDebug()

    if projectname is None:
        projectname = BaseTools.getTestCaseName()
    
    Project.CreateCsProject(projectname,0)
    
    
    Project.setContent([projectname,'assets','main.qml'],'debugqml.qml')
    
    if sys.platform == "linux2" or "6.2" in platform.version():
        UI.view.QmlEditor.setBreakPoint('main.qml',7,146)
    else:
        UI.view.QmlEditor.setBreakPoint('main.qml',5,128)
       
    

    Debug.debugQml(projectname)
           
            
    Main.quit()
   
   

