import Messages_Declear as Messages_Declear
import ftplib
def internet_tool():
    import webbrowser
    result = webbrowser.open("www.beaconos.org")
    if result:
        print ("-", Messages_Declear.WeHaveInternet)
    else:
        print("-", Messages_Declear.InternetNotAviliable)
        return EOFError
def get_pkg(package_name):
    path = "/home/ftp/applications"
    cmd = "RETR" + package_name
    ftp = ftplib.FTP('IP ADDRESS')
    ftp.login('BeaconOS','theLawnMower.epic') #Change
    ftp.cwd(path)
    ftp.retrbinary(cmd,open(package_name, 'wb').write)
