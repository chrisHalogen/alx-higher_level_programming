#!/usr/bin/python3
"""2. POST an email #0"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    email = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(email).encode("ascii")
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
