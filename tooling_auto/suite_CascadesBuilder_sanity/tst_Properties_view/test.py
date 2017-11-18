"""
@summary:Test  QML Property  View

"""

import imp
imp.load_source("None", findFile("scripts", "AddPath.py"))


import os
from BaseTools import  BaseTools
import Main
import Project

import UI.view.Outline
import UI.view.QmlProperty
import UI.view.QmlEditor
import UI.windows.Preferences




def main(projectname=None):
    
    Main.init(os.path.realpath(__file__))
    
    Main.cleanUp()
    
    Main.startUp()
    
    UI.windows.Preferences.disableQmlFolding()
    
    
    if projectname is None:
        projectname = BaseTools.getTestCaseName()
    Project.CreateCsProject(projectname,0)
    
    Project.setContent([projectname,'assets','main.qml'],'content.qml')
    test.verify(UI.view.Outline.find(['Page','Container','Button']),"button exists in outline view")

#    update text property
    UI.view.Outline.click(['Page','Container','Button'])
    UI.view.QmlProperty.setText('button2')
    test.verify(UI.view.QmlEditor.contains('main.qml',r'text: "button2"'),"property text update in Qml Editor")
    
#    update Id property
    UI.view.QmlProperty.setId('testId')
    test.verify(UI.view.QmlEditor.contains('main.qml',r'id: testId'),"property Id update in Qml Editor")
    
    
    test.verify(UI.view.Outline.find(['Page','Container','testId (Button)']),"property Id updated in Outline view")
 
    Main.quit()
