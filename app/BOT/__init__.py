from os.path import dirname, abspath
from sys import path
root_location = dirname(abspath('app'))

try:
    path.append(root_location+'/app/var')
    from var import vars
except:
    dir = root_location.split('app')[0]
    path.append(dir+'/app/var')
    from var import vars



