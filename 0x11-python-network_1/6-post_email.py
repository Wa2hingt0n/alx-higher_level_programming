#!/usr/bin/python3
""" Sends a POST request with an email passed as the second parameter """


if __name__ == "__main__":
    import requests
    import sys

    r = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    content = r.text
    print(content)
