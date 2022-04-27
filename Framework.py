bug_status = False
status = 0
temp = 0
cp = 0
debcode = 0
debloc = 0
bgtype = 0
log = open("Debug Log.txt", 'w')
def copy(cp = 0):
    if cp == 0:
        cp = open("Copy.txt", 'w')
        cp.write("C.NS 1")
    else: 
        print("An Error, Illegal Copy")
        exit
def debug():
    try:
        import time
        import random
    except:
        print("ALERT: Major Error, Attention Needed-Missing Library")
    if debcode == 0:
        if debloc == 22 or 25:
            try:
                import time, random
            except NameError:
                print("× Main Thread Error: Unknown Naming TS=",t.ctime, "debug procedue at ", t.ctime, "Debug Failed")
                bug_status = True
                exit
        elif debloc == 29:
            try:
                import time, random
            except NameError:
                print("× Gerneral Error: Unknown Module or other TS=",t.ctime, "debug procedue start at ", t.ctime, "Debug Failed")
                bug_status = True
                exit
try: 
    import time as t
    from types import TracebackType
    from BootLoader import boot
except:
    debug()