import os,sys
import squish,test
import UI.windows.Import 
import UI.view.ProjectExplorer
import UI.view.QmlEditor
import Tool
import UI.Eclipse


currentopen = 4

def run(projectpath,assetpath):
    """
    @summary: import a project  and preview  under a given assets path
    @param projetpath: location of project
    @param assetpath: static file path of QML files 
    @attention: Use this method on Window platform
    
    """
    

    head,tail = os.path.split(projectpath)
        
    if len(tail) == 0 :
        newhead,tail = os.path.split(head)
        
    projectname = tail
        
    UI.windows.Import.importProject(projectpath)
    
    squish.snooze(30)
    
    files = Tool.getAllQmlFiles(os.path.join(projectpath,'assets',assetpath))
        
       
        
    root = UI.view.ProjectExplorer.getItem([projectname,'assets',assetpath])
       
    firstrun = True
        
    if root:
        if not root.getExpanded():
            squish.expand(root)
                            
            sum  =1
        
        for file in files:
            test.log("executing preview on QML file[" + str(sum) +"]:" + file)
            tokens = file.split(os.sep)
            index = tokens.index(assetpath)
            index = index + 1
            sum = sum + 1
            UI.view.ProjectExplorer.doubClick(tokens[index:],root)
               
                
            if firstrun:
                squish.snooze(15)
                firstrun = False
            UI.view.QmlEditor.switchToDesign(tokens[len(tokens)-1]) 
                
              
            if  sum % currentopen == 0 :
                UI.Eclipse.CloseAll()
                    
        
        test.log("complete preview on QML file" )
                     
                    
    

def runFast(projectpath,assetpathlist):
    """
    @summary: import a project  and preview  under a given assets path
    @param projetpath: location of project
    @param assetpath: static file path of QML files 
    @attention: Use this method on Mac platform
    
    """
    

    head,tail = os.path.split(projectpath)
        
    if len(tail) == 0 :
        newhead,tail = os.path.split(head)
        
    projectname = tail
        
    UI.windows.Import.importProject(projectpath)
    
    obj = squish.waitForObject(":Project Explorer_Tree")
    
    files = Tool.getAllQmlFiles(os.path.join(projectpath,'assets',*assetpathlist))
        
    rootpath = [projectname,'assets']
    
    rootpath.extend(assetpathlist)
    
    UI.view.ProjectExplorer.click(rootpath)
    
    squish.type(obj, "<Return>")
        
    
    sum =1
    firstrun = True
        
    while True :
        squish.type(obj, "<Down>")
        itemtext = UI.view.ProjectExplorer.getSelection()
        if "tst_" in itemtext:
            squish.type(obj, "<Return>")
        
        if ".qml" in itemtext:
            
            test.log("executing preview on QML file[" + str(sum) +"]:" + itemtext)
    
            if firstrun:
                squish.snooze(15)
                firstrun = False
               
            UI.view.QmlEditor.switchToDesign(itemtext) 
            squish.snooze(1)
            sum = sum +1
            
            if sum % currentopen  ==0 :
                UI.Eclipse.CloseAll()
                
            if "tst_automation_xmldatamodel_property_source" in itemtext:
                test.log("complete preview on QML file" )
                return
                    
             
        
       
  