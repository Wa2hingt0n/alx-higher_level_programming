#!/bin/bash
# Displays the status code of the response to a request to a URL
curl -s -o /dev/null -w "%{http_code}" $1
