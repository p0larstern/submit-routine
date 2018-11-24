import sys,os
fileName = sys.argv[1]
if os.path.exists(fileName):
    pass
else :
    print("File not found!")