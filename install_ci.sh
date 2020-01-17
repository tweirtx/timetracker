#!/usr/bin/env bash
pyenv update
pyenv install 3.7.6 -s
pyenv global 3.7.6
pip install Cython pyinstaller
pip install -Ur requirements.txt
