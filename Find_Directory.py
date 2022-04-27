import Layer_control as Layer_control, Messages_Declear as Messages_Declear
import time as t
import Storage_Manager as Storage_Manager
def search_layer(pd_name):
    if pd_name in Layer_control.Desktop:
        print(pd_name, "was found at Desktop")
    elif pd_name in Storage_Manager.tpa:
        print(pd_name, "was found at Docs/tpa")
    elif pd_name in Storage_Manager.tpb:
        print(pd_name, "was found at Docs/tpb")
    elif pd_name in Storage_Manager.tpc:
        print(pd_name, "was found at Docs/tpc")
    elif pd_name in Storage_Manager.known_file:
        print(pd_name,"was found at Docs/known files")
    else:
        print("f_dir:", Messages_Declear.CanNotFindFile)
        t.sleep(0.5)
        print("∆ Check if there is a typo in ", pd_name)
        t.sleep(0.5)
        print("∆ If you are using BeaconOS 1.0, try to reboot the system or change the directory to '/Docs'")
        
        print("∆ Try to run command 'fix' if you are using BeaconOS 1.2 or above")
