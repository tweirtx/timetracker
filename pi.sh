#!/usr/bin/env bash
curl pyenv.run | bash
echo "export PATH=\"~/.pyenv/bin:$PATH\"
eval \"$(pyenv init -)\"
eval \"$(pyenv virtualenv-init -)\"
" >> ~/.bashrc
~/.bashrc
pyenv install 3.6.7
sudo apt install libpq-dev libmariadbclient-dev freetds-dev -y
git clone https://github.com/tweirtx/timetracker
cd timetracker
pyenv local 3.6.7
pip3 install --prefer-binary Cython # Cython takes ages to build on pi so we're trying to get a precompiled one
pip3 install -Ur requirements.txt