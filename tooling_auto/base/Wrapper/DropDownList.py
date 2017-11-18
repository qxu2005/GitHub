"""
@summary: Wrapper for Dropdown


"""

import test
import squish
import re


class DropDownList:

    @staticmethod
    def getSelection(combo):
        """
        @summary: get selected item
        @param combo: drop down list object  
        @return: selected item or None 
        """
        
        index = combo.getSelectionIndex()
        if index > -1:
            return combo.getItem(index)
        else:
            return None
    
    @staticmethod
    def find(combo,itemName):
        """
        @summary: check whether a item exists in a drop down list
        @param combo: drop down list object 
        @param itemName: item name , support regular expression
        @return:  matched item object or None
        """
        p = re.compile(itemName)
        for i in range(combo.getItemCount()):
            item = combo.getItem(i)
            if item == itemName :
                return itemName
            m = p.match(item)
            if m:
                return item
        return None
    
    
    
    
    @staticmethod
    def selectItem(combo,itemName):
        """
        @summary: select a item in a drop down list
        @param combo: drop down list object
        @param itemName: item name   
        
        """
        item = DropDownList.find(combo,itemName)
        if item is not None:
            squish.mouseClick(squish.waitForObjectItem(combo,item),0,0,0,squish.Button.NoButton)
        else :
            raise LookupError(str(itemName) + "can not be found in dropdownlist" )
            
        