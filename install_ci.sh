#!/usr/bin/env bash
GOBACKTO=$(pwd)
cd /opt/pyenv
git pull
cd $GOBACKTO
pyenv install 3.7.6 -s
pyenv global 3.7.6
pip install Cython pyinstaller
pip install -Ur requirements.txt
