from Wrapper.Tree import Tree
import squish
import test



__symbolic_name = ":Target_Navigator_Tree"


def find(path,root=None):
    ''' check given path exist in SystemInfoPerspective '''
    
    if root is None:
        root = squish.waitForObject(__symbolic_name)
       
    return Tree.find(path,root)
    
  

def deleteProject(path):
    ''' delete a tree item   '''
    
    Tree.rightClick(path,squish.waitForObject(__symbolic_name))
    squish.activateItem(squish.waitForObjectItem(":Target_Navigator_Menu", "Delete"))
    squish.clickButton(squish.waitForObject(":Confirm Delete.Also delete any associated file(s) with this target?_Button"))
    squish.clickButton(squish.waitForObject(":Confirm Delete.Yes_Button"))
    
  

def delExistingDevice():
    ''' delete a device '''
    root = squish.waitForObject(__symbolic_name)
    enabled = squish.waitFor("root.getItemCount() == 1", 50000)       
    if enabled:
        item_text = root.getItem(0).getText()
        deleteProject([item_text])
    
    
         
    

def isProcessRunning(processname):
    ''' verify whether given process  is running '''
    
    root = squish.waitForObject(__symbolic_name)
    enabled = squish.waitFor("root.getItemCount() == 1", 20000)       
    if not enabled:
        test.fail('can not verify process in Systeminfo Perspective')
        return False
    
    item_text = root.getItem(0).getText()
   
    Tree.click([item_text],root)
   
    squish.expand(root.getItem(0))
    squish.expand(root.getItem(0))  # workaround to expand  a tree item
    regular_name = processname+'(.)'
    item = find([item_text,regular_name])
    if item:
        return True
    else:
        return False
        
    
def killTestProcess():
    ''' kill  tst_ process on device '''
    
    root = squish.waitForObject(__symbolic_name)
    enabled = squish.waitFor("root.getItemCount() == 1", 20000)       
    if not enabled:
        test.log("Can not find device in system info")
        return
    
    item_text = root.getItem(0).getText()
    Tree.click([item_text],root)
    
    squish.expand(root.getItem(0))
    squish.expand(root.getItem(0))  # workaround to expand  a tree item
    
    regular_name = "tst_.|CsProfile"
    item = find([item_text,regular_name])
    if item:
        #Tree.rightClick([item_text,item.getText()],root)
        squish.mouseClick(squish.waitForObjectItem(__symbolic_name, item.getText()), 100, 8, 0, squish.Button.Button3)
        squish.activateItem(squish.waitForObjectItem(":Target_Navigator_Menu", "Deliver Signal..."))
        squish.clickButton(squish.waitForObject(":Deliver Signal.OK_Button"))