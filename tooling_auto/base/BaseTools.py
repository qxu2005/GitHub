import os,sys
import signal
import squish
import squishinfo
import shutil
import zipfile
import subprocess


class BaseTools:
    
    @staticmethod
    def killProcess():
        """
        @summary: kill a AUT application
        
        """
        ctx = squish.currentApplicationContext()
        if ctx.isRunning:
           Utility.killProcessById(ctx.pid)
           

    @staticmethod
    def killProcessById(pid):
        """
        @summary: kill a process by id
        @param pid: process ID
        """
        if sys.platform == "win32":
             #subprocess.Popen("taskkill /F /T /PID %i"%pid,shell=False)
             os.system("taskkill /PID %i /f"%pid)
        else :
            os.kill(pid,signal.SIGKILL)


    @staticmethod
    def killProcessByName(processname):
        """
        @summary: kill a process by name
        @param processname: process name 
        """
        
        if sys.platform == "darwin":
            cmd = "ps aux | grep %s"%processname
            stdoutdata,stderrdata,returncode = BaseTools.cmdline(cmd)
            for r in stdoutdata.split('\n'):
                if cmd in r  or "grep %s"%processname in r :
                    continue
                break
            if r:
                pid = r.split()[1]
                BaseTools.killProcessById(int(pid))
                squish.snooze(5)
        elif sys.platform == "win32":
            #subprocess.Popen("taskkill /F /im %s"%processname,shell=False)
            os.system("taskkill /im %s /f"%processname)
            squish.snooze(5)
        else :
            cmd = "ps -A | grep %s"%processname
            stdoutdata,stderrdata,returncode = BaseTools.cmdline(cmd)
            for r in stdoutdata.split('\n'):
                if cmd in r  or "grep %s"%processname in r :
                    continue
                break
            if r:
                pid = r.split()[0]
                BaseTools.killProcessById(int(pid))
                squish.snooze(5)
    
    
            
    @staticmethod
    def deleteFolder(path):
        """
        @summary: delete a folder
        @param path: folder path 
        """
        if (os.path.exists(path)):
            shutil.rmtree(path)
            
    @staticmethod
    def deleteFile(path):
        """
        @summary: delete a file
        @param path: file path 
        """
        if (os.path.exists(path)):
            os.remove(path)
            
      
    @staticmethod
    def createFolder(path):
        """
        @summary: create a folder
        @param path: fodler path 
        """ 
        if not os.path.exists(path):
            os.makedirs(path)
            
    @staticmethod
    def archive(archive_name,sourcepath):
        """
        @summary: archive a folder as a zip file
        @param archive_name: zip file name
        @param sourcepath: source folder
        """
        # shutil.make_archive(archive_name,'gztar',sourcepath)
        zip = zipfile.ZipFile(archive_name,'w')
        for root,dirs,files in os.walk(sourcepath):
            for file in files:
               zip.write(os.path.join(root,file))
        zip.close()
       
       
    @staticmethod
    def cmdline(cmd):
        """
        @summary: run command line 
        @param cmd: command line
        
        """
        p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdoutdata,stderrdata = p.communicate()
        print p.returncode
        return stdoutdata,stderrdata,p.returncode

    @staticmethod
    def getTestCaseName():
        """
        @summary: return TestCase name
        """
        head,tail = os.path.split(squishinfo.testCase)
        return tail
        