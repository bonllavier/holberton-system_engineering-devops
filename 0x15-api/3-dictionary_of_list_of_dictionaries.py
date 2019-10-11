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
    url2 = 'https://jsonplaceholder.typicode.com/users'
    with urllib.request.urlopen(url2) as response:
        html = response.read()
    datuser = json.loads(html.decode('utf-8'))
    tmp_dict = {}
    content = []
    for user in datuser:
        content = []
        for item in dattod:
            if int(user['id']) == int(item['userId']):
                content.append({"username": user['username'],
                                "task": item['title'],
                                "completed": item['completed']})
        tmp_dict.update({str(user['id']): content})
    file1 = "{}.json".format("todo_all_employees")
    with open(file1, 'w') as emplo_file:
        json.dump(tmp_dict, emplo_file)
