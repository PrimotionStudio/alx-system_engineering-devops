#!/usr/bin/python3
"""
curl reddit api
"""
import requests


def number_of_subscribers(subreddit):
    """
    a documentation
    """
    ua = "linux:0x16.api.advanced:v1 (by /u/theprimotionstudio)"
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    h = {"User-Agent": ua}
    res = requests.get(url, headers=h)
    if res.status_code == 200:
        data = res.json()
        count = data["data"]["subscribers"]
        return (count)
    else:
        return (0)
