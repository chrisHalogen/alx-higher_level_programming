#!/usr/bin/python3
"""9. My GitHub!"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth_data = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth=auth_data)
    print(res.json().get("id"))
