#!/bin/bash
# Displays the body of an HTTP GET request response if status code is 200
STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" $1)

if [ "$STATUS_CODE" == "200" ]; then
    curl -s $1
fi
