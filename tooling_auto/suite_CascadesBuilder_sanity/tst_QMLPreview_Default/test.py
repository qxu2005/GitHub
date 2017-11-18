"""
@summary:Test  QML Preview on default assets folder

"""

import imp
imp.load_source("None", findFile("scripts", "AddPath.py"))


import os,sys
import QmlPreview 
from Context import Context
import Main



def main(projectname=None):
    
    Main.init(os.path.realpath(__file__))
    
    Main.cleanUp()
    
    Main.startUp()
    
    projectpath= os.path.join(Context.GetContext('configfolder'),'project','automation')
   
    QmlPreview.runFast(projectpath,['qmlsrc'])
    
