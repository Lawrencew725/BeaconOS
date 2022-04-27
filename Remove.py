from unicodedata import name
from Storage_Manager import known_file
from Storage_Manager import tpa 
from Storage_Manager import tpb 
from Storage_Manager import tpc 
import Messages_Declear as Messages_Declear
import Console_Delcear
from pathlib import Path
import os
class strictRemove:
    def __init__(self,fileName,tag):
        self.filename = fileName
        filePath = os.getcwd()
        sonPath = str(filePath) + "/" + tag + "/" + self.filename
        if os.path.exists(sonPath):
            print("rmome: Deleting ",fileName)
            os.remove(sonPath)
        else:
            print("rmove: ",Messages_Declear.CanNotFindFile)
class removeDir:
    def __init__(self,dir):
        filePath = os.getcwd()
        sonPath = str(filePath) + "/" + dir
        if os.path.exists(sonPath):
            print("rmove(s mode): Removing Directory:",sonPath)
            os.remove(sonPath)
        else:
            print("rmove(s mode):",Messages_Declear.DirectoryNotFound)
class delete:
    def __init__(self,Name,flag,tag):
        if flag in Console_Delcear.s_mod:
            removeDir(Name)
        else:
            strictRemove(Name,tag)
