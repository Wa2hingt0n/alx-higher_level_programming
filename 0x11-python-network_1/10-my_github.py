#!/usr/bin/python3
""" Takes GitHub credentials and user the API to display the user id """


if __name__ == "__main__":
    import requests
    import sys

    url = "https://api.github.com/user"
    payload = {"login": sys.argv[1]}

    r = requests.get(url, params=payload, auth=(
        sys.argv[1], sys.argv[2])).json()

    try:
        print(r['id'])
    except KeyError:
        print('None')
