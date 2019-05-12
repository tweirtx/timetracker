#!/usr/bin/env bash
sudo apt update
sudo apt dist-upgrade -y
sudo apt install libpq-dev libmariadbclient-dev freetds-dev python3 python3-pip git -y
git clone https://github.com/tweirtx/timetracker
cd timetracker
pip3 install Cython --only-binary :all: # Cython takes ages to build on pi so we're trying to get a precompiled one
pip3 install -Ur requirements.txt
echo "Would you like TimeTracker to start automatically upon boot? [y/n]"
read autoboot
if [[ ${autoboot} == 'y' ]]; then
    echo "echo Starting TimeTracker..." >> ~/.bashrc
    echo "cd timetracker && python3 -m timetracker" >> ~/.bashrc
    echo "Autobooting"
fi
