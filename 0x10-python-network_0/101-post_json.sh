#!/bin/bash
# 8. cURL a JSON file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
