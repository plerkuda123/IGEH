import os

print(" + UPDATE ")
os.remove("givi32")
os.remove("givi64")
os.system("git pull")
os.system("chmod +x givi32 givi64")
os.remove("update.py")
exit("done")
