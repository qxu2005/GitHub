import squish
import object


def importProject(projectpath):
    ''' importe a given project ''' 
    
    squish.activateItem(squish.waitForObjectItem(":C/C++ - QNX Momentics IDE_Menu", "File"))
    squish.activateItem(squish.waitForObjectItem(":File_Menu", "Import..."))
    squish.expand(squish.waitForObjectItem(":Import_Tree", "General"))
    squish.mouseClick(squish.waitForObjectItem(":Import_Tree", "Existing Projects into Workspace"),15,15,0, squish.Button.Button1)
    squish.clickButton(squish.waitForObject(":Import.Next >_Button"))
    squish.type(squish.waitForObject(":Import.Select root directory:_Text"), projectpath)      
    squish.type(squish.waitForObject(":Import.Select root directory:_Text"), "<Return>")
    squish.snooze(1)
    squish.mouseClick(squish.waitForObject(":Import.Copy projects into workspace_Button"),15,15,0,squish.Button.Button1)
    squish.clickButton(squish.waitForObject(":Import.Finish_Button"))
    squish.waitFor('not object.exists(":Import.Finish_Button")',60000)
    
    
