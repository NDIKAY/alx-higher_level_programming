#!/bin/bash
# This script sends a request to 0.0.0.0:5000/catch_me and receives a response with "You got me!" in the body.
curl -s -L -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 54.209.116.64:5000/catch_me
