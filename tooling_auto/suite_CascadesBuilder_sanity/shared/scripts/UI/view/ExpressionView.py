import squish
import test



def __addNewExpression(varname):
    ''' add a variable in  expression view '''
    
    squish.mouseClick(squish.waitForObjectItem(":Expressions_Tree", "Add new expression"), 76, 15, 0, squish.Button.Button1)
    try:
        squish.type(squish.waitForObject(":Expressions_Text",2000), varname)
    except:
        squish.mouseClick(squish.waitForObjectItem(":Expressions_Tree", "Add new expression"), 76, 15, 0, squish.Button.Button1)
        squish.type(squish.waitForObject(":Expressions_Text"), varname)
    squish.type(squish.waitForObject(":Expressions_Text"), "<Return>")
    
    

def __getExpressionValue(treeitem):
    ''' get variable value from expression view '''
    
    squish.mouseClick(squish.waitForObjectItem(":Expressions_Tree",treeitem), 15, 15, 0, squish.Button.Button1)
    result = squish.waitForObject(":Expressions_StyledText").getText()
    return result
     
     

def expressionCompare(varname,treeitem,expectvalue):
    ''' verify variable value is same as exprssion view '''
    __addNewExpression(varname)
    value = __getExpressionValue(treeitem)
    if  not expectvalue in value :
        test.fail('variable:' + varname + " is not showed up correctly in ExpressionView : Expect:" +expectvalue + "Actual:"+value)
    else:
        test.passes('verified on variable ' + varname)
    
    squish.mouseClick(squish.waitForObjectItem(":Expressions_Tree", "Add new expression"), 76, 15, 0, squish.Button.Button1) 
    

def removeExpression():
    ''' remove all variables from expression view '''
    squish.mouseClick(squish.waitForObject(":Remove All Expressions_ToolItem"), 15, 15, 0, squish.Button.Button1)
    squish.clickButton(squish.waitForObject(":Remove All Expressions.Yes_Button"))