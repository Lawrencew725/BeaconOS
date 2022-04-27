import Messages_Declear as md
import New_MShell as nms
from pathlib import Path
hangup = False
class threadingTool:
    def __init__(self,name):
        path = Path(name)
        if path:
            pass
        else:
            print(md.NoSuchFile)
    def run(self):
        global hangup
        threadType = nms.threads.isDaemon()
        if threadType == True:
            hangup = True
        else:
            hangup = False