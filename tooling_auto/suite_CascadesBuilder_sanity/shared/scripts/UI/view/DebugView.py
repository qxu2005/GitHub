from Wrapper.Tree import Tree
import UI.Eclipse
import squish
import test

    
    

def find(path,root=None):
    ''' looking for path in Debug Tree '''
    
    if root is None:
         root = squish.waitForObject(":Debug_Tree")  
    item= Tree.find(path,root)
    
    if item :
        return True
    else:
        return False
    
    

def isSuspendedAt(msg):
    ''' verify whether given msg matches  selected info from Debug Tree '''
    
    selectmsg = Tree.getSelection(squish.waitForObject(":Debug_Tree"))
    if selectmsg:
        return  msg in selectmsg
    return False
    
    
    

def resumeDebug():
    ''' click Resume button '''
    
    squish.waitForObject(':Resume_ToolItem', 20000)
    squish.mouseClick(squish.waitForObject(":Resume_ToolItem", 20000), 15, 15, 0, squish.Button.Button1)
         
    
def stepInto():
    ''' click step into button '''
    squish.waitForObject(":Step Into_ToolItem", 20000)
    squish.mouseClick(squish.waitForObject(":Step Into_ToolItem"), 15, 15, 0, squish.Button.Button1)
        
  
def stepOver():
    ''' click Step Over button '''
    squish.waitForObject(":Step Over_ToolItem", 20000)
    squish.mouseClick(squish.waitForObject(":Step Over_ToolItem"), 15, 15, 0, squish.Button.Button1)
        
   
def stepReturn():
    ''' click Step Return button '''
    squish.waitForObject(":Step Return_ToolItem", 20000)
    squish.mouseClick(squish.waitForObject(":Step Return_ToolItem"), 15, 15, 0, squish.Button.Button1)
        
   
def disconnect():
    ''' click Disconnect  button '''
    squish.waitForObject(":Disconnect_ToolItem", 20000)
    squish.mouseClick(squish.waitForObject(":Disconnect_ToolItem"), 15, 15, 0, squish.Button.Button1)
        
 

def isResumAble():
    '''verify  Resume button is enable '''
    
    obj = squish.waitForObject(":Resume_ToolItem",20000)
    enabled = squish.waitFor("obj.getEnabled()== 1 ", 60000)      
    return enabled
    

def valueEqual(varname,value):
    ''' verify value equal  in variable tree'''
    
    squish.doubleClick(squish.waitForObjectItem(":Variables_Tree", varname), 15, 15, 0, squish.Button.Button1)
    realvalue= squish.waitForObject(":Variables_StyledText").getText()
    if not realvalue==value:
        test.fail(varname + ' is not equal ' + value + "real value is " + realvalue)
    else:
        test.passes('verified variable '  + varname)
    
    

def valueContains(varnamepath,value):
    ''' verify value contains in variable tree '''
    
    rootnode = squish.waitForObject(":Variables_Tree")
    Tree.doubClick(varnamepath,rootnode,rootnode)
    realvalue= squish.waitForObject(":Variables_StyledText").getText()
    if not  value in realvalue:
        test.fail(str(varnamepath) + ' is not equal ' + value + "real value is " + realvalue)
    else:
        test.passes('verified variable '  + str(varnamepath))
    
    

def setValue(varname,value):
    ''' set  variable value   '''
    
    squish.mouseClick(squish.waitForObjectItem(":Variables_Tree", varname), 15, 15, 0, squish.Button.Button3)
    squish.activateItem(squish.waitForObjectItem(":Variables_Menu", "Change Value..."))
    squish.type(squish.waitForObject(":Set Value_Shell"),value)
    squish.clickButton(squish.waitForObject(":Set Value.OK_Button"))
       
    

def waittingForTerminated():
    ''' verify whether  "terminated"  shows up in Debug tree '''
     
    UI.Eclipse.stop()
    enabled = squish.waitFor("find(['<terminated>.']) == True", 30000)     
    return enabled
        

def toggleVariablesWindow():
    ''' maxim/minimum  variable window '''
    
    squish.doubleClick(squish.waitForObject(":Debug_Variables_CTabItem"), 15, 15, 0, squish.Button.Button1)
    