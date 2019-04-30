#!/usr/bin/env bash
if [echo "$TRAVIS_OS_NAME" == "osx"]; then
    curl https://pyenv.run | bash
fi;
pyenv install 3.7.3 && pyenv global 3.7.3