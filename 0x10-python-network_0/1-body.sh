#!/bin/bash
# Script to fetch the body of a 200 status code response from a URL
curl -s -L -w "%{http_code}" -o /dev/null "$1" | grep -q "200" && curl -s "$1"
