#!/bin/bash
# Script to fetch the body of the response from a URL and display its size in bytes
curl -s "$1" | wc -c

