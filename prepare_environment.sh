#!/bin/bash

brew install libgeoip

python3 -m venv .
source ./bin/activate
pip3 install ip2geotools numpy scipy matplotlib
pip3 install --user git+https://github.com/matplotlib/basemap.git
deactivate
