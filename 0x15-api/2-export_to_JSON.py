#!/usr/bin/python3
""" A module that request data from an API and
export as json file """
import json
import requests
import sys



if __name__ == "__main__":
    id = sys.argv[1]

    r = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(id))
    n = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}".format(id))

    content = n.json()
    name = content[0]["username"]
    content_todo = r.json()
    main_dict = {}
    task_list = []
    for todo in content_todo:
        task_detail = {}
        task_detail["task"] = todo["title"]
        task_detail["completed"] = todo["completed"]
        task_detail["username"] = name
        task_list.append(task_detail)
    main_dict[id] = task_list

    with open('{}.json'.format(id), 'w', encoding='UTF8') as jsonfile:
        json.dump(main_dict, jsonfile)
