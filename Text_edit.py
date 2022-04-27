import Storage_Manager as Storage_Manager, Messages_Declear as Messages_Declear
from pathlib import Path
import os
tager = 0
def sedt(fileName,fileTag):
    name = str(fileName)
    tager = fileTag
    Storage_Manager.tag()
    if tager in Storage_Manager.tag_a:
        Storage_Manager.tpa.append(name)
        fatherPath = os.getcwd()
        sonPath = str(fatherPath) + "/tpa" + "/" + name
    elif tager in Storage_Manager.tag_b:
        Storage_Manager.tpb.append(name)
        fatherPath = os.getcwd()
        sonPath = str(fatherPath) + "/tpb" + "/"  + name
    elif tager in Storage_Manager.tag_c:
        Storage_Manager.tpc.append(name)
        fatherPath = os.getcwd()
        sonPath = str(fatherPath) + "/tpc" + "/"  + name
    else:
        Storage_Manager.known_file.append(name)
        fatherPath = os.getcwd()
        sonPath = str(fatherPath) + "/others" + "/"  + name
    doc = open(sonPath, 'w')
    while True: 
        try:
            index1 = str(input("|t| "))
            doc.write(index1)
            doc.write('\n')
        except EOFError:
            print('\n')
            break
class editAgain:
    def __init__(self, fileName):
        try:
            path = Path(fileName).absolute()
            file = open(path, 'r+')
            lines = file.readlines()
            for lines in file:
                print(lines)
            while True:
                try:
                    inputs = str(input("|t| "))
                    file.write('\n')
                    file.write(inputs)
                    file.write('\n')
                except EOFError:
                    break
        except FileNotFoundError:
            print("mdf: ", Messages_Declear.CanNotFindFile)
            pass
