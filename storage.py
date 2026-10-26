import json


FILENAME = 'tasks.json'


def save_tasks(tasks):
    with open(FILENAME,'w',encoding = 'utf-8') as file:
        json.dump(tasks, file, ensure_ascii = False, indent = 4)