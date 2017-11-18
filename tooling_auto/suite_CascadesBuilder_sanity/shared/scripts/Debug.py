"""
@summary: all functions need by Debug test

"""


import sys,os,platform
import squish
import object
import test

import Project
import UI.view.DebugView
import UI.Eclipse
import UI.view.ExpressionView
import UI.view.QmlEditor
import UI.windows.Perspective

from Context import Context


__DebugDelay =40000


def _debugAtMain(projectname):
    
    if Context.GetContext('DEVICE') =='NONE':
        test.fail('can not connect to device/simulator')
        return False
    
    if Context.GetContext('DEVICE') =='Simulator':
        Project.setActiveBuildConfiguration(projectname,'4 Simulator-Debug')
        Project.buildActiveProject()
           
    
    Project.launchDebug(projectname)
         
    flag = UI.view.DebugView.isResumAble()
    
    if not flag:
         test.fail("can not get resumable during debug project", projectname)
         UI.Eclipse.stop()
         return False
    else:
        test.passes('can get resumable during debug project ' + projectname)
 
    flag = squish.waitFor('UI.view.DebugView.isSuspendedAt("main() at main.cpp")', __DebugDelay)
    if not flag:
         test.fail ("can not suspend at main()")
         UI.Eclipse.stop()
         return False
    else:
        test.passes('can suspend at main()')
     
    return True
    
    

def debugQml(projectname):
    
    result = _debugAtMain(projectname)
   
    if not result :
        return
    
    UI.view.DebugView.resumeDebug()
   
    flag = squish.waitFor('UI.view.DebugView.isSuspendedAt("main.qml onCreationCompleted() line:")', __DebugDelay)
    if not flag:
         test.fail ("can not suspend at QML file")
         return 
    else:
         test.passes('can suspend at QML file')
    
    UI.view.DebugView.stepInto()
    
    squish.snooze(2)
    
    UI.view.DebugView.stepOver()
    
    UI.view.DebugView.valueEqual('x','Undefined')
    
    UI.view.DebugView.stepOver()
    
    UI.view.DebugView.valueEqual('x','10')
        
    UI.view.DebugView.stepOver()
    
    UI.view.DebugView.valueEqual('x','11')   
    
    UI.view.DebugView.stepOver()
    
    UI.view.DebugView.valueEqual('x','10') 
    
    UI.view.DebugView.stepOver()
    
    UI.view.DebugView.stepOver()
    
    UI.view.DebugView.valueEqual('y','18') 
    
    UI.view.DebugView.setValue('y','20')
    
    UI.view.DebugView.valueEqual('y','20') 
    
    UI.view.DebugView.stepOver()
    
    UI.view.DebugView.valueEqual('y','30') 
    
    UI.view.DebugView.stepOver()
    
    
    UI.Eclipse.showExpressionView()
    
    UI.view.ExpressionView.expressionCompare('l1.text','"l1.text"','done')
    

    if sys.platform == "darwin":
        UI.view.QmlEditor.hoverTo('main.qml',93, 263)
    elif sys.platform == "linux2":
        UI.view.QmlEditor.hoverTo('main.qml',102, 174)
    elif "6.2" in platform.version():
        UI.view.QmlEditor.hoverTo('main.qml',106, 160)
    else:
        UI.view.QmlEditor.hoverTo('main.qml',88, 170)
    
    
    test.verify(UI.view.QmlEditor.treeExists(['l1.text']),'l1.text does show up in hover context window')

    test.verify('done' in UI.view.QmlEditor.getValueInfo() ,'l1.text value does  show up correctly in hover context window')
    
    if sys.platform == "darwin":
        UI.view.QmlEditor.openEvaluate('main.qml',93, 263)
    elif sys.platform == "linux2":
        UI.view.QmlEditor.openEvaluate('main.qml',102, 174)
    elif  "6.2" in platform.version():
        UI.view.QmlEditor.openEvaluate('main.qml',106, 160)
    else:
        UI.view.QmlEditor.openEvaluate('main.qml',88, 170)

   
    test.verify( UI.view.QmlEditor.treeExists(['object','accessibility']),'accessibility does  show up in Evaluate context window')
    
  
    UI.view.QmlEditor.treeClick('text')
    test.verify('done' in UI.view.QmlEditor.getValueInfo() ,'text value does  show up correctly in Evaluate context window')
  
       
    test.verify(UI.view.DebugView.waittingForTerminated(),'terminate debug application')  
    
                


def debugJs(projectname):
    
    result = _debugAtMain(projectname)
   
    if not result :
        return
    
    UI.view.DebugView.resumeDebug()
    
    flag = squish.waitFor('UI.view.DebugView.isSuspendedAt("test.js update() line:")', __DebugDelay)   
    if not flag:
         test.fail ("can not suspend at Js file")
         return
    else:
         test.passes('can suspend at Js file')
    
    UI.view.DebugView.valueEqual('y','28') 
    UI.view.DebugView.valueEqual('z','1')
    UI.view.DebugView.valueEqual('x','10')
    
    
    UI.Eclipse.showExpressionView()
    
    UI.view.ExpressionView.expressionCompare('y','"y"','28')
    
    
    test.verify(UI.view.DebugView.waittingForTerminated(),'terminate debug application')  
    
    
    
def reDebug(projectname,x,y):
   
    result = _debugAtMain(projectname)
   
    if not result :
        return
    
    UI.view.DebugView.resumeDebug()
       
    flag = squish.waitFor('UI.view.DebugView.isSuspendedAt("main.qml onCreationCompleted() line:")', __DebugDelay)   
    if not flag:
         test.fail ("can not suspend at QML file")
         return
    else:
        test.passes('can suspend at QML file')

    UI.view.DebugView.stepInto()
    
    squish.snooze(2)
    
    UI.view.DebugView.stepOver()
    
    UI.view.DebugView.valueEqual('x','Undefined')
    
    UI.view.DebugView.stepOver()
    
    UI.view.DebugView.valueEqual('x','10')
    
    UI.windows.Perspective.openQMLPerspective()
    
    if sys.platform == "linux2":
        UI.view.QmlEditor.rePlaceContent('main.qml','var x = 10','var x = 28')
       
    else:
        context = UI.view.QmlEditor.getContext('main.qml')
    
        UI.view.QmlEditor.setFileContext(context.replace('var x = 10','var x = 28'),'main.qml')
                
        UI.view.QmlEditor.setBreakPoint('main.qml',x,y)
    
    UI.Eclipse.launchDebug()
    
      
#    flag = squish.waitFor("UI.view.DebugView.find(['<terminated>.']) == True", 30000)
#
#    if not flag:
#         test.fail("can not get terminate app during redebug project", projectname)
#         return

            
            
    flag = UI.view.DebugView.isResumAble()
    
    if not flag:
         test.fail("can not get resumable during redebug project", projectname)
         return
    else:
        test.passes('can  get resumable during redebug project')
 
    flag = squish.waitFor('UI.view.DebugView.isSuspendedAt("main() at main.cpp")', __DebugDelay)
    if not flag:
         test.fail ("can not suspend at main() during redebug")
         return
    else:
        test.passes('can  suspend at main() during redebug')

    UI.view.DebugView.resumeDebug() 
    flag = squish.waitFor('UI.view.DebugView.isSuspendedAt("main.qml onCreationCompleted() line:")', __DebugDelay)
    if not flag:
         test.fail ("can not suspend at QML file during redebug")
         return
    else:
        test.passes('can suspend at QML file during redebug')

    UI.view.DebugView.stepInto()
    
    squish.snooze(2)
    
    UI.view.DebugView.stepOver()
    
    UI.view.DebugView.valueEqual('x','Undefined')
    
    UI.view.DebugView.stepOver()
    
    UI.view.DebugView.valueEqual('x','28')
    
    test.verify(UI.view.DebugView.waittingForTerminated(),'terminate debug application')  
        
        

def setCppBreakPoint(path,lineno):
    UI.windows.Perspective.openQMLPerspective()
    Project.openFile(path)
    
    
    if sys.platform == "darwin":
        #squish.nativeType("<Command+l>")
        UI.view.QmlEditor.inputKey(path[len(path)-1],"<Command+l>")
    else:
        #squish.nativeType("<Ctrl+l>")
        UI.view.QmlEditor.inputKey(path[len(path)-1],"<Ctrl+l>")
     
    squish.type(squish.waitForObject(":Go to Line_Shell"),lineno)  
    squish.clickButton(squish.waitForObject(":Go to Line.OK_Button")) 
    
    if sys.platform == "darwin":
        #squish.nativeType("<Command+Shift+b>")
        UI.view.QmlEditor.inputKey(path[len(path)-1],"<Command+Shift+b>")
    else :
        #squish.nativeType("<Ctrl+Shift+b>")
        UI.view.QmlEditor.inputKey(path[len(path)-1],"<Ctrl+Shift+b>")
        
    UI.windows.Perspective.openDebugPerspective()
    
    
    

def debugNative(projectname,path,lineno):
    
    result = _debugAtMain(projectname)
   
    if not result :
        return

    setCppBreakPoint(path,lineno)
    
    UI.view.DebugView.resumeDebug() 
    flag = squish.waitFor('UI.view.DebugView.isSuspendedAt("ApplicationUI::ApplicationUI() at applicationui.cpp:")', __DebugDelay) 
    if not flag:
         test.fail ("can not suspend at cpp file")
         return
    else:
        test.passes('can suspend at cpp file')
    
    UI.view.DebugView.toggleVariablesWindow()
    
    UI.view.DebugView.valueContains(['char_c'],"Details:99 'c'")
    
    UI.view.DebugView.valueContains(['bool_true'],"Details:true")
    
    UI.view.DebugView.valueContains(['char_p','\*char_p'],"Details:99 'c'")
    
    UI.view.DebugView.valueContains(['myints'],"Details:{1, 2, 3, 4}")
    
    
    
    UI.view.DebugView.toggleVariablesWindow()
    
     
    test.verify(UI.view.DebugView.waittingForTerminated(),'terminate debug application')  
        
        
        
        
        
        
def debugQtypes(projectname,path,lineno):
    
    result = _debugAtMain(projectname)
   
    if not result :
        return

    setCppBreakPoint(path,lineno)
    
    UI.view.DebugView.resumeDebug() 
    flag = squish.waitFor('UI.view.DebugView.isSuspendedAt("ApplicationUI::ApplicationUI() at applicationui.cpp:")', __DebugDelay)    
    if not flag:
         test.fail ("can not suspend at cpp file")
         return
    else:
        test.passes('can suspend at cpp file')
    
    UI.Eclipse.showExpressionView()
    
    UI.view.ExpressionView.expressionCompare('myChar0','myChar0','Details:"7"')
  
     
    test.verify(UI.view.DebugView.waittingForTerminated(),'terminate debug application')  
        
        

        
        
def debugPrettyPrinting(projectname,path,lineno):
    
    result = _debugAtMain(projectname)
   
    if not result :
        return
    
    setCppBreakPoint(path,lineno)
    
    UI.view.DebugView.resumeDebug() 
    flag = squish.waitFor('UI.view.DebugView.isSuspendedAt("ApplicationUI::ApplicationUI() at applicationui.cpp:")', __DebugDelay) 
    if not flag:
         test.fail ("can not suspend at cpp file")
         return 
    else:
        test.passes('can suspend at cpp file')
    
    
    UI.Eclipse.showExpressionView()
    
    UI.view.ExpressionView.expressionCompare("qString0", "qString0", 'Details:"Hello"')
  
    UI.view.ExpressionView.expressionCompare("qbytearry0", "qbytearry0", "rock & roll")
    
    UI.view.ExpressionView.expressionCompare("qlist0", "qlist0",'QList<QString> = {[0] = "one", [1] = "two", [2] = "three"}')
  
    UI.view.ExpressionView.expressionCompare("qstringlist0", "qstringlist0",'QStringList<QString> = {[0] = "Bill Murray", [1] = "John Doe", [2] = "Bill Clinton"}')
                                                    
     
    UI.view.ExpressionView.expressionCompare("qqueue0", "qqueue0","QQueue<int> = {[0] = 1, [1] = 2, [2] = 3}")
    
    UI.view.ExpressionView.removeExpression()
    
    UI.view.ExpressionView.expressionCompare("qvector0", "qvector0",'QVector<QString> = {[0] = "one", [1] = "two", [2] = "three"}')
    
    UI.view.ExpressionView.expressionCompare("qstack0", "qstack0","QStack<int> = {[0] = 1, [1] = 2, [2] = 3}")
    
    UI.view.ExpressionView.expressionCompare("qlinkedlist0", "qlinkedlist0",'QLinkedList<QString> = {[0] = "one", [1] = "two", [2] = "three"}') 
    
    UI.view.ExpressionView.expressionCompare("qmap0", "qmap0",'QMap<QString, int> = {["one"] = 1, ["three"] = 3}')
    
    UI.view.ExpressionView.expressionCompare("qmutimap0", "qmutimap0",'QMultiMap<QString, int> = {["plenty"] = 2000, ["plenty"] = 100}')
    
    UI.view.ExpressionView.removeExpression()
    
    
    UI.view.ExpressionView.expressionCompare("qhash0","qhash0",'QHash<QString, int> = {["one"] = 1, ["thirteen"] = 0, ["seven"] = 7, ["three"] = 3, ["twelve"] = 12}')

    UI.view.ExpressionView.expressionCompare("qmultihash0","qmultihash0",'QMultiHash<QString, int> = {["plenty"] = 5000, ["plenty"] = 2000, ["plenty"] = 100}')

    UI.view.ExpressionView.expressionCompare("qdate0", "qdate0", "1995-05-17")
    
    UI.view.ExpressionView.expressionCompare("qtime0", "qtime0", "14:00:00.000")
    
    UI.view.ExpressionView.expressionCompare("dateTime0", "dateTime0", "1998-01-01 00:01:02.000")
    
    UI.view.ExpressionView.removeExpression()
    
    UI.view.ExpressionView.expressionCompare("url0", "url0","http://qt.nokia.com/List%20of%20holidays.xml")
                 
    UI.view.ExpressionView.expressionCompare("qsetiterator0", "qsetiterator0",'QSet<QString> = {[0] = "one"}')
    
    UI.view.ExpressionView.expressionCompare("myChar0", "myChar0", '"7"')
    
     
    test.verify(UI.view.DebugView.waittingForTerminated(),'terminate debug application')     
        

        