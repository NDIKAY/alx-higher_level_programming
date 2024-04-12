#!/bin/bash
# Script to send a JSON POST request to a URL passed as the 
curl -s -H "Content-Type: application/json" -X POST -d @"$2" "$1"
