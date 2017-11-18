"""
@summary:Test QT  native Types

"""

import imp
imp.load_source("None", findFile("scripts", "AddPath.py"))

import os
import Main
import Project
import UI.view.QmlEditor
import Debug

from BaseTools import  BaseTools




def main(projectname=None):
    
    Main.init(os.path.realpath(__file__))
    
    Main.cleanUp()
    
    Main.startUp()
    
    Main.createTarget()
   

    if projectname is None:
        projectname = BaseTools.getTestCaseName()
    
    Project.CreateCsProject(projectname,0)
    
    
    Project.setContent([projectname,'src','applicationui.cpp'],'qtype.cpp')
   
    Debug.debugQtypes(projectname,[projectname,'src','applicationui.cpp'],"201")
   
    Main.quit()
           
            
        
   
   

