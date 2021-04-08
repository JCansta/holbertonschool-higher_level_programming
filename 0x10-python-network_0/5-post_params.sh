#!/usr/bin/bash
# Takes the URL send a POST request and display the body
curl -sLX POST --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" $1
