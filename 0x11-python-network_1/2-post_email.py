#!/usr/bin/python3
""" Takes a URL and email address as an argument, sends a POST request to the
    URL and sisplays the body of the response
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        content_dec = content.decode()
        print(content_dec)
