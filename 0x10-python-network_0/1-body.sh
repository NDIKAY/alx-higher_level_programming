#!/bin/bash
# Script to fetch the body of a 200 status code response from a URL, following any redirections
curl -s -L "$1" | grep -o '<body.*' | tail -n +1
