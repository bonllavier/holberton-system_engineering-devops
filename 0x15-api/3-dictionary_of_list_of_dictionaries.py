#!/usr/bin/python3
# task 1
import json
import sys
import urllib.request

if __name__ == "__main__":
    numbertask = 0
    taskcomplete = 0
    tasksdone = []
    url1 = 'https://jsonplaceholder.typicode.com/todos'
    with urllib.request.urlopen(url1) as response:
        html = response.read()
    dattod = json.loads(html.decode('utf-8'))
    with urllib.request.urlopen('https://jsonplaceholder.typicode.com/users') as response:
        html = response.read()
    datuser = json.loads(html.decode('utf-8'))
    tmp_dict = {}
    content = []
    for user in datuser:
        for item in dattod:
            content.append({"task": item['title'],
                        "completed": item['completed'],
                        "username": user['username']})
        tmp_dict = {user['id']: content}
    file1 = "{}.json".format("todo_all_employees")
    with open(file1, 'w') as emplo_file:
        json.dump(tmp_dict, emplo_file)
