import sys
import squish,object
import UI.Eclipse
from Wrapper.Tree import Tree


def switchToDesign(filename):
    ''' switch to Preview '''
    if sys.platform == "linux2":
        inputKey(filename,"<Ctrl+Shift+2>")
    else:
        UI.Eclipse.InputKey("<Ctrl+Shift+2>")
     
      
     

def setFileContext(content,filename):
    ''' set new content for a given file '''
    
    obj = __getStyleText(filename)
    obj.setText(content)
    UI.Eclipse.SaveAll()
            

def getContext(filename):
    ''' get context info  '''
    
    obj = __getStyleText(filename)
    return obj.getText()
                
            
            

def dragDrop(filename,componentsname):
    ''' drag drop from component view to QML editor '''
    
    obj = __getStyleText(filename)
    squish.dragAndDrop(squish.waitForObject(componentsname), 29, 24, obj, 86, 79, squish.DnD.DropCopy)
            
            
            

def switchToIconView():
    ''' switch to Icon view in Component view '''
    
    squish.mouseClick(squish.waitForObject(":Icon View_ToolItem"), 15, 15, 0, squish.Button.Button1)
        
        

def contains(filename,txt):
    ''' check info exists in QML editor '''
    
    obj = __getStyleText(filename)
    info = obj.getText()
    return txt in info
    
    
def tabExist(tabname):
    ''' check whether tab exists in QML editor '''
    TabItemInfo ="{caption='"+ tabname+ "' type='org.eclipse.swt.custom.CTabItem' window=':C/C++ - QNX Momentics IDE_Shell'}"
    return object.exists(TabItemInfo)

def __getStyleText(filename):
    ''' get Object from a given file name '''
    
    TabItemInfo ="{caption?='*"+ filename+ "' type='org.eclipse.swt.custom.CTabItem' window=':C/C++ - QNX Momentics IDE_Shell'}"
    StyledTextInfo = "{container= " +TabItemInfo +"  isvisible='true'  type='org.eclipse.swt.custom.StyledText'}"
    styletext = squish.waitForObject(StyledTextInfo)
    return styletext
    

def __getEvaluateMenu(filename):
    ''' open Evaluate menu in debug session '''
    
    TabItemInfo ="{caption?='*"+ filename+ "' type='org.eclipse.swt.custom.CTabItem' window=':C/C++ - QNX Momentics IDE_Shell'}"
    StyledTextInfo = "{container= " +TabItemInfo +"  isvisible='true'  type='org.eclipse.swt.custom.StyledText'}"
    menuinfo ="{container=" + StyledTextInfo+ "  menuStyle='SWT.POP_UP' type='org.eclipse.swt.widgets.Menu'}"
    menu = squish.waitForObject(menuinfo)
    return menu
    
    
def inputKey(filename,key):
    obj = __getStyleText(filename)
    squish.type(obj, key)
    
def setBreakPoint(filename,x,y):
    ''' set break point in QML editor '''
    
    TabItemInfo ="{caption?='*"+ filename+ "' type='org.eclipse.swt.custom.CTabItem' window=':C/C++ - QNX Momentics IDE_Shell'}"
    qmlCanvasInfo = "{basetype='org.eclipse.swt.widgets.Canvas' container=" + TabItemInfo + "isvisible='true' occurrence='4'}"
    qmlCanvas = squish.waitForObject(qmlCanvasInfo)
    squish.doubleClick(qmlCanvas, x, y, 0, squish.Button.Button1)
      
      
def rePlaceContent(filename,old,new):
    obj = __getStyleText(filename)
    squish.type(squish.waitForObject(obj), "<Ctrl+f>")
    squish.type(squish.waitForObject(":Find/Replace.Find:_Combo"), old)
    squish.type(squish.waitForObject(":Find/Replace.Replace with:_Combo"), new)
    squish.clickButton(squish.waitForObject(":Find/Replace.Replace All_Button"))
    squish.clickButton(squish.waitForObject(":Find/Replace.Close_Button"))
    UI.Eclipse.SaveAll()
       
    
def hoverTo(filename,x,y):
    ''' trigger hover in QML Editor '''
    
    obj = __getStyleText(filename)
    squish.mouseMove(obj,x,y)
    squish.snooze(5)
        

def treeExists(path):
    '''  check  given path exists in  the tree of hover/evaluate window '''
    
    root = squish.waitForObject(":_Tree")
    item= Tree.find(path,root)
    if item :
         return True
    else:
        return False
    

        
    
def treeClick(itemname):
    '''  click  given itemname  in  the tree of hover/evaluate window '''
    squish.doubleClick(squish.waitForObjectItem(":_Tree", itemname), 15, 15, 0, squish.Button.Button1) 
   

def getValueInfo():
    '''  get styledText in hover/evaluate window '''
    obj = squish.waitForObject(':_StyledText')
    return obj.getText()
    
    

def openEvaluate(filename,x,y):
    ''' trigger evaluate window '''
    
    obj = __getStyleText(filename) 
    squish.doubleClick(obj, x, y, 0, squish.Button.Button1)   
    squish.mouseClick(obj, x, y, 0, squish.Button.Button3)
    obj = __getEvaluateMenu(filename)
    squish.activateItem(squish.waitForObjectItem(obj, "Evaluate"))
    squish.snooze(5)
        