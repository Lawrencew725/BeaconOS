# BeaconOS
This is the source code of BeaconOS
## Introduction To This Project
  BeaconOS is a operating system that is a **Embedded Linux Project** that is based on Buildroot(www.buildroot.org)
  This project is purely made with Python3.10.0(www.python.org)
## How to Use This Project
  Please go to the official website for this project: www.beaconos.org and visit "User Center" to download all instructions and quick start handbook
## How to Load the System?
  This file sctructure of BeaconOS is mingrated from BASH, all of the system files are stored under the following directory: `/etc/profile.d`
  - All of your script file will be stored under: `/etc/profile.d/scripts`.
  - Text File will be stored under: `/etc/profile.d/tpa` or `/etc/profile.d/tpb`, `/etc/profile.d/tpc`, `/etc/profile.d/others`
  - If the OS did not load after the boot and Buildroot ask for your username and password, use the following:
            UserName: root
            No password provided
  After your login action, the OS should load. Otherwise, enter the following command: `cd /etc/profile.d && python3 New_MShell.py`
