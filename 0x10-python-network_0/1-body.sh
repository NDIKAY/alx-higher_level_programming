#!/bin/bash
# Script to fetch the body of a 200 status code response from a URL, handling redirections
curl -s -L "$1" -o response.tmp && grep "HTTP/1.1 200 OK" response.tmp && cat response.tmp
