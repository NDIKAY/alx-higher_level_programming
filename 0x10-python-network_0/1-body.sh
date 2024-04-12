#!/bin/bash
# Script to fetch the body of a 200 status code response from a URL
curl -s -o body.tmp -w "%{http_code}" "$1" | grep -q "200" && cat body.tmp

