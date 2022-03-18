#!/usr/bin/python3
""" Takes a URL, sends a request and displays the body of the response """


if __name__ == "__main__":
    import urllib.request
    import sys
    from urllib.error import HTTPError

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            content = response.read().decode()
            print(content)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
