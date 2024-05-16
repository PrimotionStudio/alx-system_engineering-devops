#!/usr/bin/python3
"""
curl reddit api
"""
import json
import requests


def top_ten(subreddit):
    """
    a documentation
    """
    try:
        ua = "alx"
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        h = {"User-Agent": ua}
        res = requests.get(url, headers=h)
        if res.status_code == 200:
            data = res.json()
            j = 0
            for i in data["data"]["children"]:
                if j < 10:
                    print(i["data"]["title"])
                else:
                    break
                j += 1
        else:
            raise requests.exceptions.RequestException
    except (
        requests.exceptions.RequestException,
        KeyError,
        json.decoder.JSONDecodeError,
    ):
        return None
