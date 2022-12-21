#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf run')
except:
    pass
	
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('run'):
        os.system('curl -L https://github.com/givi-xd/IGEH/blob/main/givi32?raw=true -o run') 
        os.system("chmod +x run")
        os.system("./run")
    else:
        os.system("./run")

elif bit == '32bit':
    if not os.path.isfile('run'):
        os.system('curl -L https://github.com/givi-xd/IGEH/blob/main/givi32?raw=true -o run') 
        os.system("chmod +x run")
        os.system("./run")
    else:
        os.system("./run")
