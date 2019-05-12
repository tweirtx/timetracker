#!/usr/bin/env bash
sudo apt install libpq-dev libmariadbclient-dev freetds-dev -y
git clone https://github.com/tweirtx/timetracker
cd timetracker
pip3 install --prefer-binary Cython # Cython takes ages to build on pi so we're trying to get a precompiled one
pip3 install -Ur requirements.txt