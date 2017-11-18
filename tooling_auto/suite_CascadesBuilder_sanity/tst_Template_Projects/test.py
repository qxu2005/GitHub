"""
@summary:Test All available Cascades template Projects
        build,launch ,terminate 

"""


import imp
imp.load_source("None", findFile("scripts", "AddPath.py"))


import os
import Main
import Project
from BaseTools import  BaseTools
from Context import Context



def main(projectname=None):

    Main.init(os.path.realpath(__file__))
    
    Main.cleanUp()
    
    Main.startUp()
    
    Main.createTarget()
   
    count = Project.GetCsTemplateCount()
    
    
    for index in range(0,count):
        projectname = "template"+str(index)
        
        Project.CreateCsProject(projectname,index)
        
        Project.verifyCS4ProjectCreated(projectname)
        
        Project.verifyCS4ProjectBuild(projectname,'1 Device-Debug')
        Project.verifyCS4ProjectBuild(projectname,'4 Simulator-Debug')
        Project.verifyCS4ProjectBuild(projectname,'3 Device-Release')
        
        
        if Context.GetContext('DEVICE') =='NONE':
            test.fail('can not connect to device/simulator')
            Main.quit()
            return
        
        
        Project.launch(projectname)
        
        Project.verifyIsRunning(projectname)
       
        Project.stop()
        
        Project.verifyIsTerminated(projectname)
        
        Project.closeProject(projectname)
            
    Main.quit()
   
   

