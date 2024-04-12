#!/bin/bash
# Script to fetch thie body of the response from a URL and display its size in bytes
curl -s "$1" | wc -c
