##############################################################################################
#                                    What is Installer                                       #
# This is the early loading script for BeaconOS dev-1.6.x or above                           #
# This will install all the required modules when the user first load BeaconOS               #
# If any OS fix has been requested, BeaconOS will communicate with the server: get this file #
# Do notice that this file will be removed when installing is finished.                      #
##############################################################################################
alias py="python3"
if cd /etc/profile.d/TP_Supports
then
    if py get_pip.py
    then
        echo "<BeaconOS-Com>Installing Required Modules"
        if pip3 install tk
        then
            echo "<BeaconOS-Com> Installation progress: 1/2"
            if pip3 install Keyborard
            then
                echo "<BeaconOS-Com> Installation progress: 2/2"
            else
                echo "<BeaconOS-Err> Module is NOT Installed Properly: Exception Localtion: /pip3 install Keyboard/"
                poweroff
            fi
        else
            echo "<BeaconOS-Err> Module is NOT installed Properly: Exception Localtion: /pip3 install tk/"
            poweroff
        fi
    else
        echo "<BeaconOS-Err> Unknown File Structure"
    fi 
fi
if chmod -u+X /etc/profile.d/EarlyLoader.sh
then
    echo "Loading OS from Defualt Early Loader"
    sh /etc/profile.d/EarlyLoader.sh
fi
if cd .. && echo "<BeaconOS-Com> Removing installation media file..." && rm /etc/profile.d/Installer.sh
then
    echo "<BeaconOS-Com> Removal Success"
else
    echo "<BeaconOS-Err> Unable to remove installation media file: Exception Location: /..&& rm/etc/profile.d/Installer.sh/"
fi