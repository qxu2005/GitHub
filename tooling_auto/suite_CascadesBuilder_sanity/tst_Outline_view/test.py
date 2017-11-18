"""
@summary:Test  QML Outline View

"""

import imp
imp.load_source("None", findFile("scripts", "AddPath.py"))


import os
from BaseTools import  BaseTools
import Main
import Project

import UI.view.Outline
import UI.view.QmlProperty
import UI.windows.Preferences


def main(projectname=None):
    
    Main.init(os.path.realpath(__file__))
    
    Main.cleanUp()
    
    Main.startUp()
    
    UI.windows.Preferences.disableQmlFolding()
    
    if projectname is None:
        projectname = BaseTools.getTestCaseName()
        
        
    Project.CreateCsProject(projectname,1)
    
    Project.setContent([projectname,'assets','main.qml'],'content.qml')
    
    
    test.verify(UI.view.Outline.find(['Page','Container','Button']),"button exists in outline view")
    
    test.verify(UI.view.Outline.find(['Page','Container','l1 (Label)']),"lable l1 exists in outline view")
    
    
    UI.view.Outline.click(['Page','Container','Button'])
    text =  UI.view.QmlProperty.getText()
    test.verify(text=='button', 'button match outline and property view')
        
        
    UI.view.Outline.click(['Page','Container','l1 (Label)'])
    text = UI.view.QmlProperty.getText()
    test.verify(text=='label1', 'label match outline and property view')
    
    Main.quit()
