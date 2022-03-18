#!/usr/bin/python3
""" Lists 10 commits from most recent to oldest of the repository rails
    owned by the user rails
"""


if __name__ == "__main__":
    import requests
    import sys

    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    content = r.json()

    try:
        for i in range(10):
            print("{}: {}".format(content[i].get("sha"),
                                  content[i].get("commit").get(
                                      "author").get("name")))
    except IndexError:
        pass
