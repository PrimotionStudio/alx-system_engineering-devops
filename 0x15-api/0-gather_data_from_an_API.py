#!/usr/bin/python3
"""
 Python script that, using REST API,
 for a given employee ID, returns
 information about his/her TODO list progress.
"""
import requests
import json
from sys import argv


emp_id = argv[1]
# Employee name
url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
res = requests.get(url)
if res.status_code != 200:
	print("Failed:", res.status_code)
	exit()
# Employees Todos
url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(emp_id)
_res = requests.get(url)
if _res.status_code != 200:
	print("Failed:", _res.status_code)
	exit()
total = 0
comp = 0
for todo in _res.json():
	if todo["completed"] == True:
		comp += 1
	total += 1
# print("Total of {} Employees".format(_res.json()))
# for attr in res.json().__iter__():
# 	print("{} => {}".format(attr, type(res.json().__iter__().__dir__())))
# 	print()
# print(res.json().items())
# print(dict(res.json()).__dir__())
# for k, v in dict(res.json()).items():
# 	print("{} => {}".format(k, v))
# 	print()
print("Employee {} is done with tasks({}/{}):".format(dict(res.json())["name"], comp, total))
for todo in _res.json():
	if todo["completed"] == True:
		print("\t {}".format(todo["title"]))