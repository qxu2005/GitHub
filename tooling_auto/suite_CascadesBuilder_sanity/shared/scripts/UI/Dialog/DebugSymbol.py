import re
import squish
import object
from Context import Context
import test

    
def downloadSymbol():
    '''   download runtime symbol  if necessary '''
    
    enabled = squish.waitFor('object.exists(":Missing Debug Symbols.Yes_Button")',15000)
        
    if not enabled:
        return False
        
    squish.clickButton(squish.waitForObject(":Missing Debug Symbols.Yes_Button"))
   
    squish.waitFor('object.exists(":Installing runtimes....Run in Background_Button")',10000)     
   
    info =''
    while object.exists(":Installing runtimes....Run in Background_Button"):
        obj = squish.waitForObject(":Installing runtimes....info_Label")
        info = info + obj.getText()
        squish.snooze(5)
            
    substring = re.findall(r"runtime\.\d+\.\d+\.\d+\.\d+$",info)
    if len(substring) > 0:
        Context.AddContext("runtime", substring[0])
        test.log("download new runtime:" + substring[0] )
    else:
        test.log("Error happens on  downloading symbol :" + info )
        
    return True