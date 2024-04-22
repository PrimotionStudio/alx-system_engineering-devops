#!/usr/bin/python3
"""
extend your Python script to
export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    res = requests.get(url)
    if res.status_code != 200:
        print("Failed:", res.status_code)
        exit()
    with open("todo_all_employees.json", "w") as f:
        f.write("")
    records = {}
    for user in res.json():
        user_id = user["id"]
        username = user["username"]
        tasks = []
        url = "https://jsonplaceholder.typicode.com/todos?userId={}"
              .format(user_id)
        _res = requests.get(url)
        if _res.status_code != 200:
            print("Failed:", _res.status_code)
            exit()
        for todo in _res.json():
            task = {"username": username, "task": todo["title"],
                    "completed": todo["completed"]}
            tasks.append(task)
        records.update({str(user_id): tasks})

    with open("todo_all_employees.json", "a") as f:
        json.dump(records, f)
