#!/usr/bin/env bash
rm -rf build dist
pyinstaller -F timetracker.spec
dist/timetracker