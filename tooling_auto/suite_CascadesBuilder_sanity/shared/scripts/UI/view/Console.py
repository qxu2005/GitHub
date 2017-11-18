import squish
import re


def consoleContains(substr):
    ''' lookinf for  info in console context '''
    
    obj = squish.waitForObject(":Console_StyledText")
    consoleinfo = obj.getText()
    
    if substr in consoleinfo:
        return True
    
    p = re.compile(substr)
    
    if p.match(consoleinfo):
        return True
    
    return False
    