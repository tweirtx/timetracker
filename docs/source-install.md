# Installation from source
If you don't trust binaries or they don't work for your system, don't worry! This project is 
designed to be easy to run from source.

## Install Python
Install Python 3. I only test on 3.7 right now, but others should work fine. If you're on Windows,
download from [here](https://python.org/download/windows). On Linux or MacOS, I suggest looking at
[pyenv](https://github.com/pyenv/pyenv-installer) to manage Python installations on your system.

## Obtain the source
To run from source, you must have the source. The quickest way to get it is to run ```git clone
https://github.com/tweirtx/timetracker```. You can also download the zip or tar.gz archives.

## Install dependencies
Run ```pip3 install -Ur requirements.txt``` in the timetracker folder. If you get an error about
missing Cython, simply run ```pip3 install Cython``` and then attempt installation again.

## Run it!
To run timetracker in console mode, just run ```python3 -m timetracker``` from the timetracker folder.
For the web version, run ```python3 -m timetracker --web``` from the timetracker folder.
