"""
@summary:Test Drag/Drop  QML components from Components View

"""

import imp
imp.load_source("None", findFile("scripts", "AddPath.py"))


import os
from BaseTools import  BaseTools
import Main
import Project
import QmlComponent
import UI.windows.Preferences



def main(projectname=None):
    
    Main.init(os.path.realpath(__file__))
    
    Main.cleanUp()
    
    Main.startUp()
    
    UI.windows.Preferences.disableQmlFolding()
    
    if projectname is None:
        projectname = BaseTools.getTestCaseName()
    Project.CreateCsProject(projectname,0)
    
    QmlComponent.dragDrop(projectname)
    
    
    
    Main.quit()
