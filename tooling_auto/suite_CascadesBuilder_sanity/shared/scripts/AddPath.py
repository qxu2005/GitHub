"""
@summary:  append some folders to system path 

"""

import sys,os

suitepath =  os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(os.path.join(os.path.dirname(suitepath),'base'))
sys.path.append(os.path.join(suitepath,'shared','scripts'))


