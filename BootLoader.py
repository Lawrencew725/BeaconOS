#                                       READ ME!!!!!
# This Bootloader for BeaconOS is aviliable for versions with CC Shell ONLY
# Which means your BeaconOS verion should be: "BeaconOS dev-1.x"
# If your BeaconOS Version is: "BeaconOS dev-2.x" no matter for what CPU/Board(x/a) and what copy
# This BootLoader is NOT aviliable for you
# Using this BootLoader might causing some OS module not be imported correctly
import os
import sys
import Messages_Declear as Messages_Declear
from pathlib import Path
import New_MShell
import time 
import datetime
f3path = Path("New_MShell.py").absolute()
def boot_time():
    boot_time = datetime.datetime.today()
    print("BeaconOS load at: ", boot_time)
    time.sleep(1)
def boot():
    fpath = Path("CopyRightStatment.txt").absolute()
    statment = open(fpath, "r")
    indexa = statment.readlines
    for indexa in statment:
        print(indexa)
    auth_boot = str(input("Beacon is ready to load, type y or Y to continue >>"))
    continueboot = ["y", "Y"]
    refuseboot = ["n", "N"]
    if auth_boot in continueboot:
        exec(open(f3path).read())
    elif auth_boot in refuseboot:
        print("BootLoader:",Messages_Declear.UserRefusal)
        time.sleep(1)
        if os.system("poweroff"):
            pass
        else:
            sys.exit()
    else:
        print("BootLoader:",Messages_Declear.InvalidInput)
def reboot():
    os.system("reboot")
def short_reboot():
    boot()
boot_time()
boot()