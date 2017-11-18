"""
@summary:Test Cascades Profile

"""

import imp
imp.load_source("None", findFile("scripts", "AddPath.py"))


import os,sys
import QmlPreview 
from Context import Context
import Main
import UI.windows.Import
import Project
import CS4Profile
import UI.Eclipse



def main(projectname=None):
    
    Main.init(os.path.realpath(__file__))
    
    Main.cleanUp()
    
    Main.startUp()
    
    Main.createTarget()
    
    projectname = "CsProfile"
    
    projectpath= os.path.join(Context.GetContext('configfolder'),'project',projectname)
   
    UI.windows.Import.importProject(projectpath)
    
    UI.Eclipse.setActiveProject()
    
    
    if Context.GetContext('DEVICE') =='Simulator':
        Project.setActiveBuildConfiguration(projectname,'4 Simulator-Debug')
    else:
        Project.setActiveBuildConfiguration(projectname,'1 Device-Debug')
        
    Project.buildActiveProject()
        
    if Context.GetContext('DEVICE') =='NONE':
        test.fail('can not connect to device/simulator')
        return
        
    
    result = CS4Profile.launchProfile(projectname)
    
    if result:
        CS4Profile.verifyProfile(projectname)
    
    Project.stop()
        
    Project.verifyIsTerminated(projectname)
    
    Main.quit()
    
