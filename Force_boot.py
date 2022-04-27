import BootLoader as BootLoader
import Framework as Framework
def fboot():
        if Framework.bug_status == True:
            statement_true = ["Y", "y", "Yes", "yes"]
            statement_false = ["N", "n", "No", "no"]
            usr_statement = str(input("Beacon OS has a Major Error that requires your attendtion, type yes or y to force boot the target error >> "))
            if usr_statement in statement_true:
                try:
                    BootLoader.boot()
                except NameError:
                    print("Naming Error Occured in Boot.py")
                    force_boot = str(input("Force Boot? >>"))
                    if force_boot in statement_true:
                        boot_status = True
                    elif force_boot in statement_false:
                        boot_status = False
                        print("Force Boot Refused")
                    else:
                        print("Invalid Input")
            elif usr_statement in statement_false:
                print("Froce Boot Refused by User")
                boot_status = False
            else:
                print("NULL: force boot failed")
        else:
            print("Unable to perform a force boot")