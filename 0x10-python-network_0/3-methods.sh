#!/bin/bash
# Takes the URL and display all HTTP methos the server will accept
curl -sI $1 | grep Allow | cut -d " " -f2-
