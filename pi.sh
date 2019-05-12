#!/usr/bin/env bash
curl pyenv.run | bash
pyenv install 3.6.7
sudo apt install libpq-dev libmariadbclient-dev freetds-dev -y
git clone https://github.com/tweirtx/timetracker
cd timetracker
pyenv local 3.6.7
pip3 install Cython --prefer-binary # Cython takes ages to build on pi
pip3 install -Ur requirements.txt