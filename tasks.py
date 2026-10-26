

def add_task(tasks, name):
    tasks.append(name)
    

def show_task(tasks):
    for number, task in enumerate(tasks, start = 1):
        print(f"{number}. {task}")