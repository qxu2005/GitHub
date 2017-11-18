import os
from BaseTools import BaseTools

class Context:
    '''Represents Framework context '''
    info = {}
    
    @staticmethod
    def  AddContext(key,value):
        """
        @summary:  add a new key/value 
        @param key: key 
        @param value: value  
        
        """
        Context.info[key] = value
            
    @staticmethod
    def  GetContext(key):
        """
        @summary: get key value
        @param key:key
        @return: key value , NONE if  key does not exist 
        """
        
        if Context.info.has_key(key):
            return Context.info[key]
        else:
            return "NONE"
    
    
    @staticmethod
    def  init(testcasefullpath):
        """
        @summary: set up initial value based on test case path
        @param testcasefullpath: path of test case  
        
        """
        testcasepath = os.path.dirname(testcasefullpath)
        suitepath = os.path.dirname(testcasepath)
            
        resultpath = os.path.join(suitepath,'runfolder','Results')
        Context.AddContext("resultpath", resultpath)
            
            
        BaseTools.deleteFolder(Context.GetContext("resultpath"))
        BaseTools.createFolder(Context.GetContext("resultpath"))
            
    

        xmlpath = os.path.join(suitepath,'runfolder','Results','result.xml')
        Context.AddContext("xmlpath", xmlpath)
            
        htmlpath = os.path.join(suitepath,'runfolder','Results','result.html')
        Context.AddContext("htmlpath", htmlpath)
            
        configpath = os.path.join(suitepath,'runfolder','Config','config.xml')
        Context.AddContext('configpath',configpath)
            
            
        configfolder = os.path.join(suitepath,'runfolder','Config')
        Context.AddContext('configfolder',configfolder)
            
        loggerpath = os.path.join(suitepath, 'runfolder', 'Results', 'automation.log')
        Context.AddContext("loggerpath", loggerpath)
            
        historypath = os.path.join(suitepath, 'runfolder', 'History')
        Context.AddContext("historypath", historypath)
            