#!/bin/bash
# Displays the body of an HTTP GET request response if status code is 200
if [ $(curl -s -o /dev/null -w "%{http_code}" $1) == "200" ];then curl -s $1;fi
