#!/usr/bin/python3
""" A module that request data from an API and
export as CSV file """
import requests
import sys
import csv


if __name__ == "__main__":

    id = sys.argv[1]

    r = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(id))
    n = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}".format(id))
    content = n.json()
    name = content[0]["username"]
    content_todo = r.json()
    details = []
    for todo in content_todo:
        detail = []
        userid = id
        detail.append(userid)
        detail.append(name)
        status = todo["completed"]
        detail.append(status)
        detail.append(todo["title"])
        details.append(detail)

    with open('{}.csv'.format(id), 'w', encoding='UTF8') as csvfile:
        my_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        my_writer.writerows(details)
