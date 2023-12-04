#!/bin/bash
#a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sX POST -H "Content-Type:Application/json" -d @"$2" "$1"
