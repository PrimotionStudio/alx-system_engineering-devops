#!/usr/bin/python3
"""
def recurse(subreddit, hot_list=[])
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    a documentation
    """
    try:
        ua = "alx"
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        h = {"User-Agent": ua}
        res = requests.get(url, headers=h)
        if res.status_code == 200:
            data = res.json()
            count = data["data"]["subscribers"]
            return hot_list
        else:
            raise requests.exceptions.RequestException
    except (
        requests.exceptions.RequestException,
        KeyError,
        json.decoder.JSONDecodeError,
    ):
        return None
