#!/usr/bin/python3
"""6. POST an email #1"""
import sys
import requests


if __name__ == "__main__":
    value = {"email": sys.argv[2]}
    response = requests.post(sys.argv[1], data=value)
    print(response.text)
