#!/usr/bin/python3
"""
curl reddit api
"""
import json
import requests


def number_of_subscribers(subreddit):
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
            return count
        else:
            raise requests.exceptions.RequestException
    except (
        requests.exceptions.RequestException,
        KeyError,
        json.decoder.JSONDecodeError,
    ):
        return 0
