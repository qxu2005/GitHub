import os,sys
from BaseTools import BaseTools
import test
from Context import Context
from Config import Config
import squish

def getAllQmlFiles(path):
    """
    @summary: get all QML files in a given path
    @param path: a given path
    @return:  list 
    
    """
    list=[]
    for root, dirs, files in os.walk(path):
        for file in files:
            if ".qml" in file:
                list.append( str(os.path.join(root, file)))  
    list.sort(key=str.lower)
    return list


def getFolder(folderinfo):
    """
    @summary: looking for a folder  under AUT 
    @param folderinfo: folder is looking for 
    @return:  full path if folder is found ,  None if folder is not found 
    
    """
    ctx = squish.currentApplicationContext()
    cmdline = ctx.cwd
    tokens = cmdline.split(os.sep)
    if sys.platform == "darwin":
        indx = tokens.index('Momentics.app')
        rootlist = tokens[0:indx+1]
        rootfolder = os.sep+os.path.join(*rootlist)
    else:
        dir_list = filter(lambda x: len(x) > 0, cmdline.split(os.sep))
        rootfolder = os.sep.join(dir_list[:2])
		
    for root,dirs,files in os.walk(rootfolder):
        for dir in dirs:
            if folderinfo in dir:
                return os.path.join(root, dir)
    return None


def isProjectInstalled(projectName):
    """
    @summary: verified whether project has been installed in Device/Simulator,through blackberry-deploy
    @param projectName:  project name
    @return: True |False
    
    """
    
    squish.snooze(5)
    hostfolder = getFolder('host_')
    
    if not hostfolder:
        test.fail('can not find host_* folder')
        return False
    
    if sys.platform == "darwin":
        cmd = os.path.join(hostfolder, 'darwin','x86','usr','bin','blackberry-deploy')
    elif sys.platform == "linux2":
        cmd = os.path.join(hostfolder, 'linux','x86','usr','bin','blackberry-deploy')
    else:
        cmd = os.path.join(hostfolder, 'win32','x86','usr','bin','blackberry-deploy.bat')
    
    command = cmd + ' -listInstalledApps ' + Context.GetContext('DEVICEIP')
    
    if Context.GetContext('DEVICE') == 'Simulator': 
        password =Config.getValue("Simulator", "password")
    else:
        password=Config.getValue("DeviceUsb", "password") 
        
    if password !="None" and len(password) >0 :
        command = command + '  -password ' + password
        
    #command = '/Applications/Momentics.app/host_10_2_0_15/darwin/x86/usr/bin/blackberry-deploy  -listInstalledApps 172.16.9.154 -password qaqa'

    stdoutdata,stderrdata,returncode = BaseTools.cmdline(command)
    for r in stdoutdata.split('\n'):
        if projectName in r:
            return True
    return False