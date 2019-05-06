# Installation via binary

## Download (all)
Download the latest file for your OS [here](https://github.com/tweirtx/timetracker/releases/latest).
Place it in its own folder for best results.

## Linux (excluding Raspberry Pi)
`cd` to your timetracker directory and run `sudo chmod +x timetracker-linux`. To start in console mode,
run `./timetracker-linux`. For web mode, run `./timetracker-linux --web`.

## macOS
`cd` to your timetracker directory and run `sudo chmod +x timetracker-macos`. To start in console mode,
run `./timetracker-macos`. For web mode, run `./timetracker-macos --web`.

## Windows
The first time you run timetracker, you will probably get a SmartScreen alert. This is because I 
haven't figured out code signing yet. Click on more info followed by Run Anyway. You will not
have to go through the SmartScreen process again after this. After this, you can run timetracker.exe
either by double clicking on it or by `cd`ing to your timetracker directory and running `timetracker.exe`.

For running the web server, `cd` to your timetracker directory in a command prompt and run ```timetracker.exe --web```.