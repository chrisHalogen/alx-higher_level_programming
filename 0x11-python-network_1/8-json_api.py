#!/usr/bin/python3
"""8. Search API"""
import sys
import requests


if __name__ == "__main__":
    char = "" if len(sys.argv) == 1 else sys.argv[1]
    data = {"q": char}

    res = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        r = res.json()
        if r == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.get("id"), r.get("name")))
    except ValueError:
        print("Not a valid JSON")
