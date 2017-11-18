"""
@summary:  Master Test case for Sanity Test 

"""

import exceptions
import os
import os.path

 
def main():
    list = []
    
    list.append("tst_Outline_view")
    list.append("tst_Components_view")
    list.append("tst_Properties_view")
    list.append("tst_Release")
    list.append("tst_Template_Projects")
    
    
    list.append("tst_Debug_Qml")
    list.append("tst_Debug_Js")
    list.append("tst_Debug_Redebug")
    list.append("tst_Debug_Native")
    list.append("tst_Debug_Qtypes")
    list.append("tst_Debug_PrettyPrinting")
    
    
    list.append("tst_CS4_Profile")
    list.append("tst_CS4_ReProfile")
    
    
    for test_path in list:
        test.log("Executing: %s" % test_path)
        source(os.path.join("..", test_path, "test.py"))

 
        try:
            eval("main('"+test_path+"')") # Executes the source'd test case's main() function
        except exceptions.Exception, e:
            test.fail("Error occurred in test case: %s: %s" % (test_path, e))
