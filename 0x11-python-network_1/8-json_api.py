#!/usr/bin/python3
""" Sends a POST request to 'http://0.0.0.0:5000/search_user' with a letter as
    a parameter.
"""


if __name__ == "__main__":
    import requests
    import sys

    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]

    payload = {"q": q}

    try:
        r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
        content = r.json()
        if content:
            print("[{}] {}".format(content["id"], content["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
