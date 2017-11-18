"""
@summary:Test  Cascades Project release build , deploy to device

"""


import imp
imp.load_source("None", findFile("scripts", "AddPath.py"))

import os,sys
import time
import Main
import Project
import UI.view.ProjectExplorer
from BaseTools import  BaseTools
from Context import Context
import test
import Tool

def main(projectname=None):
    

    Main.init(os.path.realpath(__file__))
    
    Main.cleanUp()
    
    Main.startUp()
    
    Main.createTarget(False)
   
    if projectname is None:
        projectname = BaseTools.getTestCaseName()
        
    
    projectname = projectname+str(int(time.time()))
    
    Project.CreateCsProject(projectname,0)
   
    Project.exportRelease(projectname)
    
    test.verify(UI.view.ProjectExplorer.find([projectname,'BAR Packages',projectname+'-1_0_0_1.bar - arm/o.le-v7']),'export released build')
        
        
    if Context.GetContext('DEVICE') =='NONE':
        test.fail('can not connect to device/simulator')
        Main.quit()
        return
    
    if sys.platform != "linux2":
        Project.installBar([projectname,'BAR Packages',projectname+'-1_0_0_1.bar - arm/o.le-v7'])
        test.verify(Tool.isProjectInstalled(projectname),'release build has been installed')
   
   
    Main.quit()
   
   

