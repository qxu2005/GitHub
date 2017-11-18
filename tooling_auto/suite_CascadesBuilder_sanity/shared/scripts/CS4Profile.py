import squish,test
import UI.view.ProjectExplorer
import UI.view.QmlEditor
import object
import Project
import os

__elapsedTime = 5

def launchProfile(projectname):
    """
    @summary: set up Profile evniorment for a project
    @param projectname: project name
    
    """
    UI.view.ProjectExplorer.rightClick([projectname])
    squish.activateItem(squish.waitForObjectItem(":Project Explorer_Tree_Menu", "Run As"))
    squish.activateItem(squish.waitForObjectItem(":Run As_Menu", "Run Configurations..."))
    
    
    squish.mouseClick(squish.waitForObjectItem(":Run Configurations_Tree", "BlackBerry C/C++ Application"), 15, 15, 0, squish.Button.Button1)
    squish.mouseClick(squish.waitForObject(":New launch configuration_ToolItem"), 15, 15, 0, squish.Button.Button1)
     
       
    squish.clickTab(squish.waitForObject(":Run Configurations.Tools_CTabItem"), 15, 15, 0, squish.Button.Button1)
    
    squish.clickButton(squish.waitForObject(":Tools.Add/Delete Tool..._Button"))
    
    
    tableWidget = squish.waitForObject(":Tools selection.Select tools to run on this launch..._Table")
    
    found = False
    for  i in range(tableWidget.getItemCount()):
        item = tableWidget.getItem(i)
        if  "Cascades Profiler" in item.getText():
            children = object.children(item)
            for child in children:
                for c in object.children(child):
                    info = squish.typeName(c)
                    if hasattr(c, "checked") and c.checked == False:
                        squish.mouseClick(c, 15, 15, 0, squish.Button.Button1)
                        found =True
    
    
    if not found:
        test.fail("can not enable profile during start up ")
        return False
    else:
        test.passes("enable profile during start up ")
        squish.clickButton(squish.waitForObject(":Tools selection.OK_Button"))
        squish.clickButton(squish.waitForObject(":Tools.Start profiling during application launch_Button"))
        squish.mouseClick(squish.waitForObject(":Run Configurations.Run_Button"), 50, 15, 0, squish.Button.Button1)
        return True
    
    
def verifyProfile(projectname):
    """
    @summary: verify profile works fine 
    @param projectname: project name
    
    """
      
     
    TabItemInfo,ElapsedToolItemInfo = __getElapsedToolItemInfo(projectname,'(0)')
    
    try:     
        squish.waitForObject(ElapsedToolItemInfo,40000)
    except:
        test.fail('can not launch profile debug')
        return
    
    test.passes("can launch profile debug")
    
    squish.snooze(__elapsedTime)
    squish.mouseClick(squish.waitForObject(ElapsedToolItemInfo), 15, 15, 0, squish.Button.Button1)
    
    squish.clickTab(squish.waitForObject(":Profile_Events_TabItem"))
    
    info = 'assets'+os.sep + '1.png'
    item = __getItemFromTable(':Profile_Events_Table',info)
    if not item:
        test.fail(info +' does not show up in events table')
    else:
        test.passes(info + ' does show up in events table')
        squish.doubleClick(item, 15, 15, 0, squish.Button.Button1)
        if UI.view.QmlEditor.tabExist('1.png'):
            test.passes('1.png has been opened correctly')
        else:
            test.fail('1.png can not be opened correctly')
        
        
    
    squish.clickTab(squish.waitForObject(TabItemInfo), 15, 15, 0, squish.Button.Button1)
    
    info = 'assets'+os.sep + 'main.qml'
    item = __getItemFromTable(':Profile_Events_Table',info)
    if not item:
        test.fail(info +' does not show up in events table')
    else:
        test.passes(info + ' does show up in events table')
        squish.doubleClick(item, 15, 15, 0, squish.Button.Button1)
        if UI.view.QmlEditor.tabExist('main.qml'):
            test.passes('main.qml has been opened correctly')
        else:
            test.fail('main.qml can not be opened correctly')
   
   



def verifyReProfile(projectname):
    """
    @summary: launch/verify profile again
    @param projectname: project name
    """
  
    TabItemInfo,ElapsedToolItemInfo = __getElapsedToolItemInfo(projectname,'(0)')
    
    try:     
        squish.waitForObject(ElapsedToolItemInfo,40000)
    except:
        test.fail('can not launch profile debug at the first time')
        return
    
    test.passes("can launch profile debug at the first time ")
    
    squish.snooze(__elapsedTime)
    squish.mouseClick(squish.waitForObject(ElapsedToolItemInfo), 15, 15, 0, squish.Button.Button1)
    
    
    Project.openFile([projectname,'assets','main.qml'])
    context = UI.view.QmlEditor.getContext('main.qml')
    
    UI.view.QmlEditor.setFileContext(context.replace(r'//add MyBtn{} here','MyBtn{}'),'main.qml')
    
    
    UI.view.ProjectExplorer.rightClick([projectname])
    squish.activateItem(squish.waitForObjectItem(":Project Explorer_Tree_Menu", "Run As"))
    squish.activateItem(squish.waitForObjectItem(":Run As_Menu", "Run Configurations..."))
    squish.mouseClick(squish.waitForObject(":Run Configurations.Run_Button"), 50, 15, 0, squish.Button.Button1)
    
    
    
    TabItemInfo,ElapsedToolItemInfo = __getElapsedToolItemInfo(projectname,'(1)')
    
    try:     
        squish.waitForObject(ElapsedToolItemInfo,40000)
    except:
        test.fail('can not launch profile debug at the 2nd time')
        return
    
    test.passes("can launch profile debug at the 2nd time ")
    
    squish.snooze(__elapsedTime)
    squish.mouseClick(squish.waitForObject(ElapsedToolItemInfo), 15, 15, 0, squish.Button.Button1)
    
    
    squish.clickTab(squish.waitForObject(":Profile_Events_TabItem_2"))
    
    info = 'assets'+os.sep + 'MyBtn.qml'
    item = __getItemFromTable(':Profile_Events_Table_2',info)
    if not item:
        test.fail(info + ' does not show up in events table')
    else:
        test.passes(info + ' does show up in events table')
        squish.doubleClick(item, 15, 15, 0, squish.Button.Button1)
        if UI.view.QmlEditor.tabExist('MyBtn.qml'):
            test.passes('MyBtn.qml has been opened correctly')
        else:
            test.fail('MyBtn.qml can not be opened correctly')
    

def __getElapsedToolItemInfo(projectname,id):
    """
    @summary: get ElapsedTool button 
    @param projectname: project name
    @param id: sequence of Tab contains ElaspedTool button   
    """
    TabItemInfo ="{caption?='"+ projectname+ "*" + id +"' type='org.eclipse.swt.custom.CTabItem' window=':C/C++ - QNX Momentics IDE_Shell'}"

    ToolBarInfo ="{container=" + TabItemInfo +  " firstItemText?='Elapsed Time:*' isvisible='true' type='org.eclipse.swt.widgets.ToolBar'}"
   
    ElapsedToolItemInfo ="{caption?='Elapsed Time: *' " + " container=" + ToolBarInfo +"  type='org.eclipse.swt.widgets.ToolItem'}"

    return TabItemInfo,ElapsedToolItemInfo

  
def __getItemFromTable(eventbable,info):
    """
    @summary: get tableItem from event table  or return None
    @param info:  matching info 
    """
    tableWidget = squish.waitForObject(eventbable)
    for  i in range(tableWidget.getItemCount()):
        item = tableWidget.getItem(i)
        if info in item.getText(0):
            return item
    return None


    
    