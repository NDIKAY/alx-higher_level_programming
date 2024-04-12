#!/bin/bash
# Script to make a request to 0.0.0.0:5000/catch_me to receive a response with th
curl -s -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" "0.0.0.0:5000/catch_me"
