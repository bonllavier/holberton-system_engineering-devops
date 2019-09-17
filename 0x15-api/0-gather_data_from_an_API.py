#!/usr/bin/python3
# task 0
import json
import sys
import urllib.request


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
        numbertask = numbertask + 1
        if item['completed'] is True:
            taskcomplete = taskcomplete + 1
            tasksdone.append(item['title'])
print("Employee {} is done with tasks({}/{}):".format(
    datuser['name'], taskcomplete, numbertask))
if taskcomplete > 0:
    for tasksdo in tasksdone:
        print("\t {}".format(tasksdo))
