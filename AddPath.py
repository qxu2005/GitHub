import sys,os

suitepath =  os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.join(suitepath,'TestBases'))
sys.path.append(os.path.join(suitepath,'TestSuites'))
sys.path.append(os.path.join(suitepath,'AppBases'))
sys.path.append(os.path.join(suitepath,'TestSuites\\*.sikuli'))
sys.path.append(os.path.join(suitepath,'Sanity'))
sys.path.append(os.path.join(suitepath,'Sanity\\*.sikuli'))
sys.path.append(os.path.join(suitepath,'AppBases\\*.sikuli'))




