#!/usr/bin/python3
"""10. Time for an interview!"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    response = requests.get(url)
    data = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                data[i].get("sha"),
                data[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
