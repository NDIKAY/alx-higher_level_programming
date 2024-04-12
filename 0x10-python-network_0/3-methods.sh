#!/bin/bash
# Script to display all HTTP methods the server will accept for a given URL
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f2-
