from glob import glob
import os
from Storage_Manager import tpa, tpb, tpc, known_file,script_file
from Layer_control import Desktop
import Messages_Declear as Messages_Declear
dekstop = ["/Desktop","/desktop"]
documents = ["/Docs", "/docs"]
def show(directory, tag):
    try:
        if directory in dekstop:
            print(Desktop)
        elif directory in documents:
            fpath = os.getcwd()
            sonPath = str(fpath) + "/" + tag
            files = os.listdir(sonPath)
            print("show: Under",tag,"BeaconOS found: ",' '.join(files))
        else:
            print("show:", Messages_Declear.DirectoryNotFound)
    except FileNotFoundError:
        print("show:",Messages_Declear.CanNotFindFile)