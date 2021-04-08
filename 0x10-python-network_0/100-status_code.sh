#!/usr/bin/bash
# Takes the URL send a POST request and display the body
curl -sw '%{http_code}' -o null $1
