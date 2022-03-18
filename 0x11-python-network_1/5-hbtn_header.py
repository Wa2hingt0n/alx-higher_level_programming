#!/usr/bin/python3
""" Sends a request to a URL and displays the value of the variable
    'X-Request-Id' in the response header
"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    content = r.headers.get("X-Request-id")
    print(content)
