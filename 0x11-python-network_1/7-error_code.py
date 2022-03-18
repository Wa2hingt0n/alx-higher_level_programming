#!/usr/bin/python3
""" Displays the HTTP status code if it's greater than or equal to 400 """


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    code = r.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        content = r.text
        print(content, end="")
