#!/usr/bin/env sh

cd /usr/local/src/vaderbot 
git pull origin master
python3.5 /usr/local/src/vaderbot/main.py
