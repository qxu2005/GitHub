import Project 
import UI.view.QmlEditor
import UI.view.Outline
import UI.Eclipse 
import squish,test



def dragDrop(projectname):
    
    """
    @summary: drag/drop some UI components from Component View to QML editor
    @param projectname: project name
    
    """
         
    UI.view.QmlEditor.switchToIconView()
         
    for i in [4,7,13,37]:
         
        Project.setContent([projectname,'assets','main.qml'],'spacecontent.qml')
        
        testcomponent="{container=':Components_CTabItem' isvisible='true' occurrence=" + "'" +str(i) +"' type='org.eclipse.swt.widgets.Canvas'}"
         
        obj  = squish.waitForObject(testcomponent)
         
        tooltipinfo = obj.getToolTipText()
         
        tokens = tooltipinfo.split('\n')
        
        UI.view.QmlEditor.dragDrop('main.qml',obj)    
         
        UI.Eclipse.SaveAll()
        
        squish.snooze(2)
         
        test.verify(UI.view.Outline.find(['Page','Container', tokens[0] ]),"drag drop component:"+tokens[0])
         
        