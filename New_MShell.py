import Run as Run 
import Remove as Remove 
import Force_boot as Force_boot
import Print_Out as Print_Out
import Layer_control as Layer_control 
import Text_edit as Text_edit
import Talk_Back as Talk_Back
import Console_Delcear as Console_Delcear
import Storage_Manager as Storage_Manager
import Find_Directory as Find_Directory
from ThreadingTool import threadingTool
import what_about as what_about
import Script_Editor as Script_Editor
import Internet_Package_Tool as Internet_Package_Tool
import help as help
import EasterEgg as EasterEgg
import Delete_Script as Delete_Script
import Time as Time
import os, sys
import time as t
import Messages_Declear as Messages_Declear
import Get_Calendar as Get_Calendar
from datetime import datetime
from pathlib import Path
import threading
easter_egg_time = ["26/2/2022", "Feb 26 2022", "Feb. 26 2022"]
reboot_declear = False
global command_components,exitSignal
exitSignal = False
powerOff = False
command_components = [ ]
clean_up = ["theHolyLight!"]
demolish = ["Demolish!","demolish!"]
exit = ["terminate me!"]
history = open("Shell_History.txt", 'w')
class demolish_OS:
    def __init__(self):
        yes = ["y", 'Yes',"yeah",'yes']
        no = ["n", 'no', "nope", "Nope", 'No']
        input = str(input("Are you sure about that? This will remove BeaconOS from your disk -> "))
        if input in yes:
            input = str(input("Let me ask you again, do you want to do it? -> "))
            if input in yes:
                os.system("cd /etc && rm profile.d")
            elif input in no:
                print("-Shell: ", Messages_Declear.UserRefusal)
            else:
                print("-Shell: ",Messages_Declear.InvalidInput)
        elif input in no:
            print("-Shell: ", Messages_Declear.UserRefusal)
        else:
            print("-Shell: ",Messages_Declear.InvalidInput)
class logicFunction:
    def __init__(self,header,target,command,flag,tag):
        self.header = header
        self.target = target
        self.command = command
        self.flag = flag
        global powerOff
        if self.header in Console_Delcear.excacute:
            Run.exc(self.target,tag)
        elif self.header in Console_Delcear.remove:
            Remove.delete(self.target,self.flag,tag)
        elif self.command in Console_Delcear.bye:
            Storage_Manager.backup()
            print("Bye")
            powerOff = True
            os.system("poweroff")
        elif self.header in Console_Delcear.reboot:
            pass
        elif self.header in Console_Delcear.short_reboot:
            pass
        elif self.header in Console_Delcear.layer:
            Layer_control.layer()
        elif self.header in Console_Delcear.creat_layer:
            Layer_control.create_layer()
        elif self.header in Console_Delcear.h_forced_boot:
            Force_boot.fboot()
        elif self.header in Console_Delcear.show:
            Print_Out.show(self.target,tag)
        elif self.header in Console_Delcear.make_document:
            Text_edit.sedt(self.target,tag)
        elif self.header in Console_Delcear.talk_back:
            Talk_Back.tk_bk(self.target)
        elif self.header in Console_Delcear.get_time:
            Time.get_time()
        elif self.header in Console_Delcear.get_calender:
            Get_Calendar.get_calender()
        elif self.header in Console_Delcear.help:
            help.cmd_help(self.target)
        elif self.header in Console_Delcear.where_is:
            Find_Directory.search_layer(self.target)
        elif self.header in Console_Delcear.what_about:
            what_about.find_file(self.target)
        elif self.header in Console_Delcear.script_editor:
            Script_Editor.scripts(self.target)
        elif self.header in Console_Delcear.Internet_Package_Tool:
            Internet_Package_Tool.get_pkg(self.target)
        elif self.command in easter_egg_time:
            EasterEgg.easteregg()
        elif self.header in Console_Delcear.remove_script:
            Delete_Script.dele_scrt(self.target)
        elif self.header in Console_Delcear.re_edit_file:
            Text_edit.editAgain(self.target)
        elif self.header in Console_Delcear.fix:
            print("Shell: OS Self-Check and Fix Requested")
            loaderPath = Path("Pre_Load.py").absolute()
            exec(open(loaderPath).read())
            print("Shell: OS Self-Check and Fix Done")
        else:
            print("Shell:",Messages_Declear.CanNotFindCommand)
class Commandsplit:
    def __init__(self,command):
        global splitedHeader,splitedTarget,splitedFlags,splitedTags
        self.command = command
        if self.command in exit:
            sys.exit()
        elif self.command in clean_up:
            os.system("clear")
        elif self.command in demolish:
            demolish_OS()
        splitedCommand = command.split()
        splitedHeader = splitedCommand[0]
        splitedTarget = splitedCommand[1]
        splitedFlags = splitedCommand[2]
        splitedTags = splitedCommand[3]
        if splitedFlags in Console_Delcear.hang_up:
            global Hangup
            Hangup = True
        else:
            Hangup = False
class MultiThreads:
    def __init__(self):
        if splitedFlags in Console_Delcear.hang_up:
            global threads
            threads = threading.Thread(target=logicFunction,args=(splitedHeader,splitedTarget,command_inputs,splitedFlags,splitedTags,),name=splitedHeader,daemon=True)
        elif splitedFlags in Console_Delcear.move_back:
            threads = threading.Thread(target=logicFunction,args=(splitedHeader,splitedTarget,command_inputs,splitedFlags,splitedTags,),name=splitedHeader,daemon=False)
        elif splitedFlags in Console_Delcear.no_flag:
            threads = threading.Thread(target=logicFunction,args=(splitedHeader,splitedTarget,command_inputs,splitedFlags,splitedTags,),name=splitedHeader,daemon=True)
        elif splitedFlags in Console_Delcear.s_mod:
            threads = threading.Thread(target=logicFunction,args=(splitedHeader,splitedTarget,command_inputs,splitedFlags,splitedTags,),name=splitedHeader,daemon=False)
        else:
            print("Shell: ",Messages_Declear.CommandSynaxError)
        threads.start()
        threads.join(timeout=2000)
class shellHistory:
    def __init__(self,input):
        self.input = input
        history.write(self.input)
        history.write('\n')
        history.write("-------------")
        history.write('\n')
class mainThread:
    def __init__(self):
        global command_inputs
        try:
            command_inputs = str(input(">>>"))
            Commandsplit(command_inputs)
            shellHistory(command_inputs)
            MultiThreads()
            print('\n',Messages_Declear.MiddleLine,'\n')
        except IndexError:
            print("Shell:",Messages_Declear.CommandSynaxError)
        except FileNotFoundError:
            print("Shell:", Messages_Declear.OSLibraryError)
            os.system("reboot")
        except ImportError:
            print("Shell:", Messages_Declear.SystemBreakdown)
        except KeyboardInterrupt:
            print('\n',Messages_Declear.MiddleLine,'\n')
            return None
        except EOFError:
            print('\n')
            pass
fpath = Path("CopyRightStatment.txt").absolute()
statment = open(fpath, "r")
indexa = statment.readlines
loaderPath = Path("Pre_Load.py").absolute()
exec(open(loaderPath).read())
print('\n')
for indexa in statment:
    print(indexa)
print('\n',Messages_Declear.StartofShell, '\n')
while True:
    mainThread()
    try:
        threadingTool(splitedTarget)
    except IndexError:
        print('\n')
        mainThread()
    except EOFError:
        mainThread()
    if powerOff == True:
        print("Poweroff: ",powerOff)
        break
os.system("poweroff")