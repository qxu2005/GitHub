import sys,os
import squish
from squish import waitForObjectItem
from squish import waitForObject
import object
from Context import Context
from Config import Config
import test
import UI.windows.Perspective
import UI.Eclipse
import UI.view.ProjectExplorer
import UI.view.Console 
import UI.windows.Export
import UI.view.SystemInfoPerspective
import UI.Dialog.DebugSymbol


def CreateCsProject(projectname,index):
    """
    @summary: create a Cascades Project
    @param projectname:  project name
    @param index: index of templates 
    
    
    """
    squish.activateItem(waitForObjectItem(":C/C++ - QNX Momentics IDE_Menu", "File"))
    squish.activateItem(waitForObjectItem(":File_Menu", "New"))
    squish.activateItem(waitForObjectItem(":New_Menu", "BlackBerry Project"))
    squish.mouseClick(waitForObjectItem(":New BlackBerry Project_List", "Application"), 0, 0, 0, squish.Button.Button1)
    squish.mouseClick(waitForObject(":New BlackBerry Project.Cascades_Label"), 0, 0, 0, squish.Button.Button1)
    squish.clickButton(waitForObject(":New BlackBerry Project.Next >_Button"))
    squish.mouseClick(waitForObjectItem(":New BlackBerry Project_Table", str(index) +"/0"), 0, 0, 0, squish.Button.Button1)
    squish.clickButton(waitForObject(":New BlackBerry Project.Next >_Button"))
    squish.type(waitForObject(":New BlackBerry Project.Project name:_Text"), projectname)
    squish.clickButton(waitForObject(":New BlackBerry Project.Next >_Button"))
    squish.clickButton(waitForObject(":New BlackBerry Project.Finish_Button"))
    enabled = squish.waitFor("object.exists(':Open Associated Perspective?.Yes_Button')",10000)
    if enabled:
        squish.clickButton(waitForObject(":Open Associated Perspective?.Yes_Button"))
    squish.waitFor("UI.view.Console.consoleContains('Build Finished') == True", 20000) 
        
    

def GetCsTemplateCount():
    """
    @summary:  get the count of available Cascades project template
    @return: count 
    
    """
    squish.activateItem(waitForObjectItem(":C/C++ - QNX Momentics IDE_Menu", "File"))
    squish.activateItem(waitForObjectItem(":File_Menu", "New"))
    squish.activateItem(waitForObjectItem(":New_Menu", "BlackBerry Project"))
    squish.mouseClick(waitForObjectItem(":New BlackBerry Project_List", "Application"), 0, 0, 0, squish.Button.Button1)
    squish.mouseClick(waitForObject(":New BlackBerry Project.Cascades_Label"), 0, 0, 0, squish.Button.Button1)
    squish.clickButton(waitForObject(":New BlackBerry Project.Next >_Button"))
    count = waitForObject(":New BlackBerry Project_Table").getItemCount()
    squish.clickButton(waitForObject(":New BlackBerry Project.Cancel_Button"))
    return count
        
        
    
        
   
                    
def verifyCS4ProjectCreated(projectName):
    """
    @summary: verify project has been created successfully
    @param projectname: project name
    """
    
    ''' Is CS4 project created? '''
    test.verify(UI.view.ProjectExplorer.find([projectName,'src','applicationui.cpp']),"applicainui.cpp has been created")
    
    test.verify(UI.view.ProjectExplorer.find([projectName,'assets','main.qml']),"main.qml has been created")
        
    test.verify(UI.view.ProjectExplorer.find([projectName,'config.pri']),"config.pri has been created")
        
        
 
def buildActiveProject():
    """
    @summary: build active project    
    
    """
        
   
    squish.mouseClick(waitForObject(":Build_ToolItem", 20000), 15, 15, 0, squish.Button.Button1)
    # Wait for 'Build Project' shell
    squish.waitFor("object.exists(':Build Project_Shell')", 20000)
    # Wait for 'Build Project' shell to dispose
    squish.waitFor("not object.exists(':Build Project_Shell')", 60000)
    
    
 
def setActiveBuildConfiguration(projectName,buildcfg):
    
    """
    @summary: set active build configuration for a project
    @param projectName: project name
    @param buildcfg: active build configuration , such as '1 Default', '2 Device-Debug'
    
    """
    UI.view.ProjectExplorer.setActiveBuildConfiguration([projectName],buildcfg)
        

    
 
def verifyCS4ProjectBuild(projectName, buildcfg):
    """
    @summary: verify whether build successfully 
    @param projectName:  project name
    @param buildcfg: active build configuration
    
    """
    
    setActiveBuildConfiguration(projectName,buildcfg)
    buildActiveProject()
    path = [projectName,'Binaries']
    if 'Device-Debug' in buildcfg:
            token = projectName +' - [arm/le]'
    elif 'Simulator-Debug' in buildcfg:
            token = projectName +' - [x86/le]'
    else:
            token = 'lib'+projectName+'.so.1.0.0 - [arm/le]'
            
    path.append(token)    
    result = UI.view.ProjectExplorer.find(path)
    if result:
            test.passes("verified_"+projectName+"_built_for_"+buildcfg)
    else:
        test.fail("failed_"+projectName+"_built_for_"+buildcfg) 
     
   
   
   
  
def openFile(path):
    """
    @summary:  open a file
    @param path: the path of file to be openned
    
    """
    UI.view.ProjectExplorer.doubClick(path)
        
    
 
def createFile(path,newfilename):
    """
    @summary: create a new file on a selected  folder
    @param path: folder to store new file
    @param newfilename: new file name
    
    """
    UI.view.ProjectExplorer.rightClick(path)
    squish.activateItem(squish.waitForObjectItem(":Project Explorer_Tree_Menu", "New"))
    squish.activateItem(squish.waitForObjectItem(":Project_New_Menu", "File"))
    squish.type(squish.waitForObject(":New File.File name:_Text"), newfilename)
    squish.clickButton(squish.waitForObject(":New File.Finish_Button"))
        
    
  
def setContent(path,contentfile):
    """
    @summary:  set a file with new content
    @param path: the file to be updated
    @param contentfile: file contains new content

    """
    UI.view.ProjectExplorer.doubClick(path)
    f = open (os.path.join(Context.GetContext('configfolder'),contentfile),'r')
    content = f.read()      
    f.close() 
    filename = path[len(path)-1]    
    TabItemInfo ="{caption?='*"+ filename+ "' type='org.eclipse.swt.custom.CTabItem' window=':C/C++ - QNX Momentics IDE_Shell'}"
    StyledTextInfo = "{container= " +TabItemInfo +"  isvisible='true'  type='org.eclipse.swt.custom.StyledText'}"
    styletext = squish.waitForObject(StyledTextInfo)
    styletext.setText(content)
    #UI.Eclipse.setFormat()
    UI.Eclipse.SaveAll()
    squish.snooze(2)
        
       
        
 
def closeProject(projectName):
    """
    @summary: close a proejct
    @param projectName:  project name

    """
 
    squish.mouseClick(waitForObjectItem(":Project Explorer_Tree", projectName, 20000), 15, 15, 0, squish.Button.Button1)
    squish.activateItem(waitForObjectItem(":C/C++ - QNX Momentics IDE_Menu", "Project"))
    squish.activateItem(waitForObjectItem(":Project_Menu", "Close Project"))
        
        
def stop():
    """
    @summary: click stop toolitem
    """
    UI.Eclipse.stop()
    
    
def launch(projectName):
    """
    @summary: launch a project
    @param projectName: project name
    
    """
    UI.view.ProjectExplorer.run([projectName])
        

def verifyIsRunning(projectName):
    """
    @summary: verify whether a project is running on device/simulator
    @param projectNmae: project name

    """
    UI.windows.Perspective.openSysInfoPerspective()
    evalinfo = 'UI.view.SystemInfoPerspective.isProcessRunning("'+projectName+'")'
    result = squish.waitFor(evalinfo, 30000)
    test.verify(result, projectName + " is launching successfully")
    UI.windows.Perspective.openQMLPerspective()
        
def verifyIsTerminated(projectName):
    """
    @summary: verify whether a project is terminated on device/simulator
    @param projectNmae: project name
    """
    UI.windows.Perspective.openSysInfoPerspective()
    evalinfo = 'UI.view.SystemInfoPerspective.isProcessRunning("'+projectName+'")'
    result = squish.waitFor(evalinfo + " == False", 30000)  
    test.verify(result, projectName + " is terminated successfully")
    UI.windows.Perspective.openQMLPerspective()


def launchDebug(projectName):
    """
    @summary: launch debug session 
    @param projectName: project name
    """
    UI.view.ProjectExplorer.debug([projectName])
    relaunch = UI.Dialog.DebugSymbol.downloadSymbol()
    if relaunch:
        UI.windows.Perspective.openQMLPerspective()
        UI.view.ProjectExplorer.debug([projectName])
    
    
    
def exportRelease(projectName):
    """
    @summary: export a release build
    @param projectName: project name
    """
    UI.view.ProjectExplorer.rightClick([projectName])
    squish.activateItem(squish.waitForObjectItem(":Project Explorer_Tree_Menu", "Export..."))
    UI.windows.Export.select(['BlackBerry','Release Build'])
    
    enabled = squish.waitFor('object.exists(":Password:_Text_Export")',10000)
    if enabled:
        squish.type(waitForObject(":Password:_Text_Export"), Config.getValue("Signing", "developerCertificatePassword"))
        squish.clickButton(waitForObject(":OK_Button"))
    
    squish.clickButton(waitForObject(":Finish_Button"))
            
    if sys.platform == "darwin" or  sys.platform == "linux2":
        enabled = squish.waitFor("object.exists(':Password:_Text_2')",30000)
    else:
        enabled = squish.waitFor("object.exists(':Password:_Text_Export')",30000)
        
    if enabled:
        if sys.platform == "darwin" or  sys.platform == "linux2":
            squish.type(waitForObject(":Password:_Text_2"), Config.getValue("Signing", "cskPassword"))
            squish.clickButton(waitForObject(":OK_Button_2"))
        else:
            squish.type(waitForObject(":Password:_Text_Export"), Config.getValue("Signing", "cskPassword"))
            squish.clickButton(waitForObject(":OK_Button"))

    
    
    squish.waitFor('object.exists(":Finish_Button") == False',30000)
    
def installBar(path):
    """
    @summary:  install a bar to device
    @param path:  path of bar file 
    """
    UI.view.ProjectExplorer.installBar(path)
    squish.waitFor("object.exists(':Install/Uninstall BAR_Shell')", 20000)
       