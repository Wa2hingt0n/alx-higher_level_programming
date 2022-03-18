#!/usr/bin/python3
""" Takes GitHub credentials and user the API to display the user id """


if __name__ == "__main__":
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    url = "https://api.github.com/user"
    credent = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    r = requests.get(url, auth=credent).json()

    print(r.get("id"))
