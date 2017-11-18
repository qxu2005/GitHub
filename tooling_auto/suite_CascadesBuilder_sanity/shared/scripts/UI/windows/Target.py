import squish
import object
import test
from Context import Context
from Config import Config
import UI.Dialog.DebugSymbol

def createBBTarget():
    ''' create Blackberry target and download runtime libs if necessary '''
    
    squish.activateItem(squish.waitForObjectItem(":C/C++ - QNX Momentics IDE_Menu", "File", 20000))
    squish.activateItem(squish.waitForObjectItem(":File_Menu", "New", 20000))
    squish.activateItem(squish.waitForObjectItem(":New_Menu", "BlackBerry Target", 20000))
    # click Auto Discover
    squish.clickButton(squish.waitForObject(":Connection.Auto Discover_Button"))
        
    button = squish.findObject(":OK_Button")
    enabled = squish.waitFor("button.enabled", 120000)
        
        
    t_table = squish.waitForObject(":Target_Table")
        
    if t_table.getItemCount() ==0:
        Context.AddContext('DEVICE','NONE')
        squish.clickButton(squish.waitForObject(":Cancel_Button"))
        squish.clickButton(squish.waitForObject(":New BlackBerry Target.Cancel_Button"))
        return
    else:
        item = t_table.getItem(0)
        if item.getText(1) == "169.254.0.1" and item.getText(0) == "USB Device" :
            Context.AddContext('DEVICE','USB')
            Context.AddContext('DEVICEIP',item.getText(1))
        elif item.getText(0) == "Simulator":
            Context.AddContext('DEVICE','Simulator')
            Context.AddContext('DEVICEIP',item.getText(1))
        else:
            Context.AddContext('DEVICE','NONE')
                 
        if Context.GetContext('DEVICE') == 'NONE':
            squish.clickButton(squish.waitForObject(":Cancel_Button"))
            squish.clickButton(squish.waitForObject(":New BlackBerry Target.Cancel_Button"))
            test.log("Can not create target")
            return
             
        squish.clickButton(squish.waitForObject(":OK_Button"))
        if Context.GetContext('DEVICE') == 'Simulator': 
            password =Config.getValue("Simulator", "password")
        else:
            password=Config.getValue("DeviceUsb", "password")
                
        if password !="None" and len(password) >0 :
            squish.type(squish.waitForObject(":Credentials.Password:_Text"), password)
                
        squish.clickButton(squish.waitForObject(":New BlackBerry Target.Finish_Button"))
        
        squish.waitFor("not object.exists(':New BlackBerry Target_Shell')", 60000)
            
        UI.Dialog.DebugSymbol.downloadSymbol()
            
             
             
             