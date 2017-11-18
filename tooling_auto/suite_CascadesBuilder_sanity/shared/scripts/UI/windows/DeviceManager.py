import squish
import test
from Context import Context
from Config import Config
import UI.windows.Perspective


def createDebugToken():
    ''' create/upload Debug Token '''
      
    squish.mouseClick(squish.waitForObject(":Device_CListCombo"), 15, 15, 0, squish.Button.Button1)
    squish.mouseClick(squish.waitForObject(":ManagerDevice"), 15, 15, 0, squish.Button.Button1)
    squish.clickButton(squish.waitForObject(":Devices.Properties_Button"))
    squish.clickButton(squish.waitForObject(":Debug Token Details..._Button"))
         
    button = squish.waitForObject(":Applicable Debug Tokens.Create..._Button")
    enabled = squish.waitFor("button.enabled", 15000)
         
    if enabled:
        squish.snooze(2)
        squish.clickButton(squish.waitForObject(":Applicable Debug Tokens.Create..._Button"))
        squish.clickButton(squish.waitForObject(":OK_Button_2"))
        squish.type(squish.waitForObject(":Password:_Text_2"), Config.getValue("Signing", "developerCertificatePassword"))
        squish.clickButton(squish.waitForObject(":OK_Button_2"))
        squish.type(squish.waitForObject(":Password:_Text_2"),  Config.getValue("Signing", "cskPassword"))
        squish.clickButton(squish.waitForObject(":OK_Button_2"))
        _table = squish.findObject(":Applicable Debug Tokens_Table")
        enabled = squish.waitFor("_table.getItemCount() == 1", 20000)
        if enabled:
            Context.AddContext('DEBUGTOKEN','READY')
        else: 
            Context.AddContext('DEBUGTOKEN','NONE')
            test.fail("can not create debug token")
    else:
        test.fail("can not create debug token")
        Context.AddContext('DEBUGTOKEN','NONE')
         
         
       
    squish.clickButton(squish.waitForObject(":OK_Button"))
    squish.clickButton(squish.waitForObject(":Properties for device.OK_Button"))
    squish.clickButton(squish.waitForObject(":Device Manager.Close_Button"))
        