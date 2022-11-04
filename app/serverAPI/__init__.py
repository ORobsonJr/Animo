from os.path import dirname, abspath
from sys import path
root_location = dirname(abspath("app"))
path.append(root_location+'/app/var')
path.append(root_location+'/app/serverAPI')
path.append(root_location+'/app/AI')

from var import vars
import machine 

