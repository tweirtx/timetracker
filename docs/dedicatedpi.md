# Setting up a dedicated Pi
If you have a Pi sitting around and you want to set up a dedicated TimeTracker station, this guide is for you.

## Initial Setup
Flash your SD card with Raspbian Lite. This is the only Pi image that TimeTracker is tested with,
other images probably work just fine but I won't be testing or fixing for other images.

Log into your Pi. The default username is `pi` with password `raspberry`

## raspi-config
You will need to make a few configuration changes to your Pi. Run `sudo raspi-config`.

* Go into the network options and connect to Wi-Fi (if applicable)
* Go into the boot options and enter Desktop / CLI. Select Console Autologin.
* Go into Localisation Settings and set your locale accordingly. You will probably need to change the keyboard layout (the default is UK). You need to set the timezone correctly as well.
* Select Finish.

## Run the configuration script
I've written a script to do the majority of the configuration for you. Run `curl https://raw.githubusercontent.com/tweirtx/timetracker/master/pi.sh | bash` to run this script.
It will take a while, especially on older Pis, so you might want to do something else for a while.

You will eventually be asked whether or not you want to autostart. This will insert a TimeTracker invocation into the startup scripts of your Pi. Enter `y` and press enter for that option,
or enter `n` and press enter to manually start TimeTracker yourself on boot.

## Reboot
Run `sudo reboot` to reboot your Pi. It should automatically start TimeTracker if you configured that.

## General usage
If you've opted for autoloading, the Pi will automatically boot into a timetracker console upon boot. To escape to a normal shell, press CTRL and C at the same time.
You will then be dropped into a normal Linux terminal. 

## Configuration
Drop into a Linux shell using the CTRL C command as mentioned above. Run `nano config timetracker/config.json` to edit the config file.