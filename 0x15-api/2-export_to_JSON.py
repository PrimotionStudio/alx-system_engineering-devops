#!/usr/bin/python3
"""
extend your Python script to
export data in the JSON format.
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

    with open(str(user_id) + ".json", "w") as f:
        f.write("")
    tasks = []
    for todo in _res.json():
        task = {"task": todo["title"],
                "completed": todo["completed"], "username": username}
        tasks.append(task)
    records = {str(user_id): tasks}
    with open(str(user_id) + ".json", "a") as f:
        json.dump(records, f)
