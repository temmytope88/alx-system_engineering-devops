#!/usr/bin/python3
""" A module that request data from an API and
export as json file """
import json
import requests


if __name__ == "__main__":

    n = requests.get(
        "https://jsonplaceholder.typicode.com/users")
    employees = n.json()
    all_employee_task = {}
    for employee in employees:
        name = employee["username"]
        id = employee["id"]
        r = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}".format(id))
        todos = r.json()
        task_list = []
        for todo in todos:
            task_detail = {}
            task_detail["username"] = name
            task_detail["task"] = todo["title"]
            task_detail["completed"] = todo["completed"]
            task_list.append(task_detail)
        all_employee_task[id] = task_list
    with open('todo_all_employees.json'.format(id),
              'w', encoding='UTF8') as jsonfile:
        json.dump(all_employee_task, jsonfile)
