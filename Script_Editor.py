import Storage_Manager as Storage_Manager, Messages_Declear as Messages_Declear
import os
python_script = ["py"]
shell_command = ["sh"]
class scripts:
    def __init__(self,fileName):
        fileType = fileName[-3:]
        if fileType == ".py":
            fatherPath = os.getcwd()
            sonPath = str(fatherPath) + "/scripts" + "/" + fileName
            pythonFile = open(sonPath,'w')
            while True:
                try:
                    userEnter = str(input("/s-p/ "))
                    pythonFile.write(userEnter)
                    pythonFile.write('\n')
                except EOFError:
                    Storage_Manager.script_file.append(fileName)
                    break
        elif fileType == ".sh":
            fatherPath = os.getcwd()
            sonPath = str(fatherPath) + "/scripts" + "/" + fileName
            shellFile = open(sonPath,'w')
            while True:
                try:
                    userEnter = str(input("/s-s/ "))
                    shellFile.write(userEnter)
                    shellFile.write('\n')
                except EOFError:
                    Storage_Manager.script_file.append(fileName)
                    break
        else:
            print("scrt_e:", Messages_Declear.FileTypeNotSupported)
