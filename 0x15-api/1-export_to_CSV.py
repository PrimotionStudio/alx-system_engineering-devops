#!/usr/bin/python3
"""
extend your Python script to
export data in the CSV format.
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    emp_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    res = requests.get(url)
    if res.status_code != 200:
        print("Failed:", res.status_code)
        exit()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)
    _res = requests.get(url)
    if _res.status_code != 200:
        print("Failed:", _res.status_code)
        exit()
    user_id = dict(res.json())["id"]
    username = dict(res.json())["username"]

    with open(str(user_id) + ".csv", "w") as f:
        f.write("")
    for todo in _res.json():
        with open(str(user_id) + ".csv", "a") as f:
            f.write('"{}","{}","{}","{}"\n'.format(user_id,
                    username, todo["completed"], todo["title"]))
