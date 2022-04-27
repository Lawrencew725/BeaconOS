import Messages_Declear as Messages_Declear, Console_Delcear
all_help = ["gt_ahp"]
def cmd_help(fst_result):
    if fst_result in Console_Delcear.excacute:
        print("exc: The command allowed you to run a script document(.py)")
    elif fst_result in Console_Delcear.reboot:
        print("rboot: Command will reboot the system")
    elif fst_result in Console_Delcear.remove:
        print("rmove: Command delete a certain file")
    elif fst_result in Console_Delcear.bye:
        print("bye: Command allowed you to shut down the system")
    elif fst_result in Console_Delcear.show:
        print("show: Command showing all the document in the current directory")
    elif fst_result in Console_Delcear.where_is:
        print("f_dir: Search files in the disk")
    elif fst_result in Console_Delcear.what_about:
        print("w_abt: Get information about a certain file")
    elif fst_result in Console_Delcear.talk_back:
        print("tk_bc: Return what you just entered")
    elif fst_result in Console_Delcear.move:
        print("move: move a certain file to another location")
    elif fst_result in Console_Delcear.layer:
        print("layer: Get your current directory")
    elif fst_result in Console_Delcear.creat_layer:
        print("cet_layer: Create a layer")
    elif fst_result in Console_Delcear.app_list:
        print("apl: Show all applications you installed")
    elif fst_result in Console_Delcear.h_forced_boot:
        print("fboot: To over run a file or bug occured")
    elif fst_result in Console_Delcear.h_forced_excacute:
        print("fexc: Over run a file or application")
    elif fst_result in Console_Delcear.make_document:
        print("mdoc: Make a document")
    elif fst_result in Console_Delcear.get_calender:
        print("gt_cal: Get the calender")
    elif fst_result in Console_Delcear.get_time:
        print("gt_tm: Get current time")
    elif fst_result in Console_Delcear.hang_up:
        print("hg_p: Put a process to back ground")
    elif fst_result in Console_Delcear.move_back:
        print("mv_b: Move a process back up")
    elif fst_result in Console_Delcear.show_thread:
        print("s_thrd: Show all process")
    else:
        print("hp:", Messages_Declear.CannotFindTarget)