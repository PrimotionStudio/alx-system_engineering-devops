#!/usr/bin/python3
"""
extend your Python script to
export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users/"
    res = requests.get(url)
    if res.status_code != 200:
        print("Failed:", res.status_code)
        exit()
    url = "https://jsonplaceholder.typicode.com/todos"
    _res = requests.get(url)
    if _res.status_code != 200:
        print("Failed:", _res.status_code)
        exit()
    user_id = dict(res.json())["id"]
    username = dict(res.json())["username"]

    with open("todo_all_employees.json", "w") as f:
        f.write("")
    tasks = []
    for todo in _res.json():
        task = {"username": username, "task": todo["title"],
                "completed": todo["completed"]}
        tasks.append(task)
    records = {str(user_id): tasks}
    with open("todo_all_employees.json", "a") as f:
        json.dump(records, f)
