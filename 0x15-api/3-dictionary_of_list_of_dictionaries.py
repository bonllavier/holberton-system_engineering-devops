#!/usr/bin/python3
# task 1
import json
import sys
import urllib.request

if __name__ == "__main__":
    numbertask = 0
    taskcomplete = 0
    tasksdone = []
    userid = sys.argv[1]
    url1 = 'https://jsonplaceholder.typicode.com/todos'
    with urllib.request.urlopen(url1) as response:
        html = response.read()
    dattod = json.loads(html.decode('utf-8'))
    with urllib.request.urlopen('https://jsonplaceholder.typicode.com/users/' +
                                sys.argv[1]) as response:
        html = response.read()
    datuser = json.loads(html.decode('utf-8'))
    for item in dattod:
        if int(item['userId']) == int(userid):
            tasksdone.append(item)
    content = []
    file1 = "{}.json".format(userid)
    for task in tasksdone:
        content.append({"task": task['title'],
                        "completed": task['completed'],
                        "username": datuser['username']})
    tmp_dict = {userid: content}
    with open(file1, 'w') as emplo_file:
        json.dump(tmp_dict, emplo_file)
