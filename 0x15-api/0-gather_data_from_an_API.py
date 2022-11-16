#!/usr/bin/python3
""" A module that request data from an API"""
import requests
import sys

if __name__ == "__main__":

    id = sys.argv[1]
    r = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(id))
    n = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}".format(id))
    content = n.json()
    name = content[0]["name"]
    content_todo = r.json()
    length = (len(content_todo))
    count_done = 0
    for todo in content_todo:
        if todo["completed"] is True:
            count_done += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, count_done, length))
    for todo in content_todo:
        if todo["completed"] is True:
            print("\t {}".format(todo["title"]))
