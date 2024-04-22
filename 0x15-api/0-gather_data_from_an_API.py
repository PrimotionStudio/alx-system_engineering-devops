#!/usr/bin/python3
"""
 Python script that, using REST API,
 for a given employee ID, returns
 information about his/her TODO list progress.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
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
    total = 0
    comp = 0
    for todo in _res.json():
        if todo["completed"] is True:
            comp += 1
        total += 1
    print("Employee {} is done \
          with tasks({}/{}):".format(dict(res.json())["name"],
                                     comp, total))
    for todo in _res.json():
        if todo["completed"] is True:
            print("\t {}".format(todo["title"]))
