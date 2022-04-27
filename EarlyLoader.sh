# This EarlyLoader file is for Loading BeaconOS
# However, this is the alternative method which is not advised
alias py='python3'
echo "Loading OS"
chmod u+x /etc./profile.d/EarlyLoader.sh
if cd /etc/profile.d #Try to direct dir to BUILDROOT file loc for BOS
then
    echo " "
else
    echo "EarlyLoader(Failure): Unknown File Structure, end of request handling"
fi
if py New_MShell.py #Try to load OS
then
    time -u
    echo "Request Handled Successfully"
else
    if python3 New_MShell.py
    then 
        echo "EarlyLoader(Alert): Defult Alias Failed, Alterntive Method Engaged"
    else
        echo "EarlyLoader(Failure): Error When Handling Request: python3 New_MShell.py"
        echo "EarlyLoader(Tip): Check the integrity of the OS"
    fi
fi