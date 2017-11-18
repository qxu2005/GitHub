"""
@summary:  open different perspective view
"""

import squish



def __open(name):
    
    squish.waitForObject(":Open Perspective_ToolItem",10000)
    squish.mouseClick(squish.waitForObject(":Open Perspective_ToolItem"), 15, 15, 0, squish.Button.Button1)
         
    tableWidget = squish.waitForObject(":Open Perspective_Table")
         
    n = tableWidget.getItemCount()
         
    for  i in range(n):
        item_text = tableWidget.getItem(i).getText()
        if name in item_text:
            squish.mouseClick(squish.waitForObjectItem(":Open Perspective_Table", str(i) +"/0"), 15, 15, 0, squish.Button.Button1)
            squish.clickButton(squish.waitForObject(":Open Perspective.OK_Button"))
            return 
          
    raise LookupError(name + "can not be found in perspective table" )   
         
    

def openSysInfoPerspective():
    __open("System Information")
        

def openCPerspective():
    __open("C/C++")
        
        

def openQMLPerspective():
    __open("QML Editing")
        
        

def openDebugPerspective():
   __open("Debug")