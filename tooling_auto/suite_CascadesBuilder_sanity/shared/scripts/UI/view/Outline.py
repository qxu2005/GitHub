from Wrapper.Tree import Tree
import squish

    

def find(path,root=None):
    ''' check given path exists in  outline view '''
    if root is None:
        root = squish.waitForObject(":Outline_Tree")
       
    item= Tree.find(path,root)
       
    if item :
        return True
    else:
        return False
   
    
    

def click(path):
    ''' click a path inside  outline view '''
    
    Tree.click(path,squish.waitForObject(":Outline_Tree"))