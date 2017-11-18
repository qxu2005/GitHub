from Wrapper.Tree import Tree
import squish

    

def find(path,root=None):
    ''' check given path exist in  Project Explorer view '''
    
    if root is None:
        root = squish.waitForObject(":Project Explorer_Tree")
       
    item= Tree.find(path,root)
    return item
    
    

def getItem(path,root=None):
    '''  looking for Tree item matching given path  in Project Explorer view '''
    if root is None:
        root = squish.waitForObject(":Project Explorer_Tree")
       
    return Tree.find(path,root)
        
    

def doubClick(path,rootnode=None):
    ''' double click a given path in Project Explorer view'''
    
    if rootnode is None:
        rootnode = squish.waitForObject(":Project Explorer_Tree")
    Tree.doubClick(path,rootnode,squish.waitForObject(":Project Explorer_Tree"))
         

def click(path):
    '''  click a given path in Project Explorer view'''
    
    Tree.click(path,squish.waitForObject(":Project Explorer_Tree"))
        

def rightClick(path):
    ''' right click a given path in Project Explorer view'''
    
    Tree.rightClick(path,squish.waitForObject(":Project Explorer_Tree"))
           
    

def getSelection():
    ''' get selected Tree item  in Project Explorer view'''
    
    return Tree.getSelection(squish.waitForObject(":Project Explorer_Tree"))
    
    

def deleteProject(path):
    ''' delete a project inProject Explorer view'''
    
    Tree.rightClick(path,squish.waitForObject(":Project Explorer_Tree"))
    squish.activateItem(squish.waitForObjectItem(":Project Explorer_Tree_Menu", "Delete"))
    squish.clickButton(squish.waitForObject(":Delete Resources.Delete project contents on disk (cannot be undone)_Button"))
    squish.clickButton(squish.waitForObject(":Delete Resources.OK_Button"))
    
    

def deleteItem(path):
    ''' delete a Tree item  in Project Explorer view'''
   
    Tree.rightClick(path,squish.waitForObject(":Project Explorer_Tree"))
    squish.activateItem(squish.waitForObjectItem(":Project Explorer_Tree_Menu", "Delete"))
    squish.clickButton(squish.waitForObject(":Delete Resources.OK_Button"))
    
   

def setActiveBuildConfiguration(path,config):
    ''' set a new active build configuration for a project '''
    
    Tree.rightClick(path,squish.waitForObject(":Project Explorer_Tree"))
    squish.activateItem(squish.waitForObjectItem(":Project Explorer_Tree_Menu", "Build Configurations"))
    squish.activateItem(squish.waitForObjectItem(":Build Configurations_Menu", "Set Active"))
    squish.activateItem(squish.waitForObjectItem(":Set Active_Menu", config))
        
    
    

def run(path):
    ''' click Run as  in Project Explorer view '''
    
    Tree.rightClick(path,squish.waitForObject(":Project Explorer_Tree"))
    squish.activateItem(squish.waitForObjectItem(":Project Explorer_Tree_Menu", "Run As"))
    squish.activateItem(squish.waitForObjectItem(":Run As_Menu", "1 BlackBerry C/C++ Application"))
         
        
        
        

def debug(path):
    '''  run Debug   in Project Explorer view '''
    Tree.rightClick(path,squish.waitForObject(":Project Explorer_Tree"))
    squish.activateItem(squish.waitForObjectItem(":Project Explorer_Tree_Menu", "Debug As"))
    squish.activateItem(squish.waitForObjectItem(":Debug As_Menu", "1 BlackBerry C/C++ Application"))
        
        
        
def installBar(path):
    ''' install Bar  in  Project Explorer view '''
    Tree.rightClick(path,squish.waitForObject(":Project Explorer_Tree"))
    squish.activateItem(squish.waitForObjectItem(":Project Explorer_Tree_Menu", "BlackBerry Tools"))
    squish.activateItem(squish.waitForObjectItem(":BlackBerry Tools_Menu", "Install"))
    
    