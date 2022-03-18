#!/usr/bin/python3
""" Fetches 'https://alx-intranet.hbtn.io/status' using the requests package
"""


if __name__ == "__main__":
    import requests

    r = requests.get("https://alx-intranet.hbtn.io/status")
    content = r.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
