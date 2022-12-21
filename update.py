import os

print(" + UPDATE ")
os.system("rm -rf givi32")
os.system("rm -rf givi64")
os.system("git pull")
os.system("git pull")
os.system("chmod +x givi32 givi64")
os.remove("update.py")
exit("done")
