#!/bin/bash
# Takes the URL and send a trquest to that URL
curl -sI "$1" | grep Content-Length | cut -d " " -f2
