from os.path import abspath, dirname
from sys import path
dir_ = dirname(abspath('app')).split('app')[0]
path.append(dir_+'/app/var')
from var.var import vars