'''
This script should be run before load in to MShell. this will make all dir and get all files if needed
'''
import os,glob
import Storage_Manager as sm
fatherPath = os.getcwd()
sonPath1 = str(fatherPath) + "/tpa"
sonPath2 = str(fatherPath) + "/tpb"
sonPath3 = str(fatherPath) + "/tpc"
sonPath4 = str(fatherPath) + "/others"
sonPath5 = str(fatherPath) + "/scripts"
if os.path.exists(sonPath1):
    pass
else: 
    os.makedirs(sonPath1)

if os.path.exists(sonPath2):
    pass
else: 
    os.makedirs(sonPath2)

if os.path.exists(sonPath3):
    pass
else: 
    os.makedirs(sonPath3)

if os.path.exists(sonPath4):
    pass
else: 
    os.makedirs(sonPath4)

if os.path.exists(sonPath5):
    pass
else: 
    os.makedirs(sonPath5)