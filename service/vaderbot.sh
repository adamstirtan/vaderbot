#!/usr/bin/env sh

export SLACK_API_KEY="INSERT SLACK API KEY HERE"
export WEATHER_API_KEY="INSERT WEATHER API KEY HERE"

cd /usr/local/src/vaderbot
git pull origin master
python3.5 /usr/local/src/vaderbot/main.py
