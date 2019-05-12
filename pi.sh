#!/usr/bin/env bash
sudo apt install libpq-dev libmariadbclient-dev freetds-dev python3 python3-pip -y
git clone https://github.com/tweirtx/timetracker
cd timetracker
pip3 install Cython --prefer-binary :all: # Cython takes ages to build on pi so we're trying to get a precompiled one
pip3 install -Ur requirements.txt
echo "echo Starting TimeTracker..."
echo "cd timetracker && python3 -m timetracker" >> .bashrc
