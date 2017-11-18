"""
@summary: Wrapper for Tree 

"""

import test
import squish
import re
import sys

class Tree:
    
    @staticmethod
    def find(path,tree_or_item,sub_path=None,verbose=False):
        """
        @summary: looking for a  path in a tree
        @param path:path to be found
        @param tree_or_item:   tree object
        @param sub_path: path to be found
        @param verbose: debug flag  
        @return: item or None
        
        """
        
        if sub_path is None:
            sub_path = path
        try:
            n = tree_or_item.getItemCount()
            if verbose:
                test.log("count:"+str(n))
        
              
            for i in range(n):
                item = tree_or_item.getItem(i)
                
                item_text = item.getText()
                
                path_element = sub_path[0]
                
                p = re.compile(path_element)
                
                if  item.getExpanded()  and  item_text != path_element:
                    squish.collapse(item)
                
                if verbose:          
                    test.log(item_text)
                  
                if item_text == path_element or p.match(item_text):
                    if verbose:
                        test.log("Found " + item_text)
         
                    if len(sub_path) == 1:
                        if verbose:
                            test.log("Find the match")
                        return item
                    else:
                        if verbose:
                            test.log("current item text:"+item.getText())
                            test.log("continue subpath")
                        squish.expand(item)
                        return Tree.find(path,item, sub_path[1:])
            if verbose:
                test.log("Error: Path element not found: " + str(sub_path[0]) + " (Complete path: " + str(path) + ")")
            return None     
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            test.log("Exception happens on:" + str(exc_type) + ":" +exc_traceback.tb_frame.f_code.co_filename +":" + str(exc_traceback.tb_lineno)  )
            return None
    
    @staticmethod
    def doubClick( path,rootnode,tree):
        """
        @summary: double click a tree item
        @param path: item path
        @param rootnode:  root node for the path
        @param tree: tree object 
        """
        item = Tree.find( path,rootnode)
        if item:
            itemBounds = item.getBounds();
            squish.doubleClick(tree, itemBounds.x + 15, itemBounds.y + 15, 0, squish.Button.Button1)
        else :
            raise LookupError(str(path) + "can not be found" )
    
    
    @staticmethod
    def doubClick_legacy(path,treename):
        """
        @summary: double click a tree item through  squish way
        @param path: item path
        @param treename: tree symbolic name  
        """
        
        for idx in range(0, len(path)-1):
            squish.expand(squish.waitForObjectItem(treename, path[idx]))
        squish.doubleClick(squish.waitForObjectItem(treename, path[len(path)-1]), 65, 7, 0, squish.Button.Button1)
        
    
    @staticmethod
    def getSelection(tree):
        """
        @summary: get selected tree item info
        @param tree: tree object 
        """
        try:
            items = tree.getSelection()
            if len(items) >0:
                return items.at(0).getText()
            else:
                return None
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            test.log("Exception happens on:" + str(exc_type) + ":" +exc_traceback.tb_frame.f_code.co_filename +":" + str(exc_traceback.tb_lineno)  )
            return None
       
      
    @staticmethod
    def click( path,tree):
        """
        @summary: click a tree item
        @param path: item path
        @param tree: tree object  
        """
        item = Tree.find( path,tree)
        if item:
            itemBounds = item.getBounds();
            squish.mouseClick(tree, itemBounds.x + 15, itemBounds.y +15, 0, squish.Button.Button1)
        else :
            raise LookupError(str(path) + " can not be found" )
    
    
    @staticmethod
    def click_legacy(path,treename):
        """
        @summary: click a tree item through squish way
        @param path: item path
        @param treename: tree symbolic name  
        """
        
        for idx in range(0, len(path)-1):
            squish.expand(squish.waitForObjectItem(treename, path[idx]))
        squish.mouseClick(squish.waitForObjectItem(treename, path[len(path)-1]), 65, 7, 0, squish.Button.Button1)
       
    
    @staticmethod
    def rightClick_legacy(path,treename):
        """
        @summary: right a tree item through squish way
        @param path: item path
        @param treename: tree symbolic name
        """
        
        for idx in range(0, len(path)-1):
            squish.expand(squish.waitForObjectItem(treename, path[idx]))
        squish.mouseClick(squish.waitForObjectItem(treename, path[len(path)-1]), 65, 7, 0, squish.Button.Button3)
        
    
    @staticmethod
    def rightClick(path,tree):
        """
        @summary: right click a tree item
        @param path:item path
        @param tree: tree object  
        """
        item = Tree.find( path,tree)
        if item:
            itemBounds = item.getBounds();
            squish.mouseClick(tree, itemBounds.x+5, itemBounds.y+5, 0, squish.Button.Button3)
           
        else :
            raise LookupError(str(path) + "can not be found" )