import Storage_Manager as sm
import Messages_Declear as Messages_Declear
import os
def dele_scrt(name):
    if name in sm.script_file:
        sm.script_file.remove(name)
        os.remove(name)
    else:
        print("rm_scrt:",Messages_Declear.CanNotFindFile)