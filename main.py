import json
FILENAME = 'tasks.txt'
def load_tasks(FILENAME):
    tasks = []
    with open(FILENAME, 'r', encoding="utf-8") as fl:
        for line in fl.readlines():
            ln = line.replace("'","\"")
            tasks.append(json.loads(ln))  #y = json.loads(x)
    return tasks

def save_tasks(tasks):
    with open(FILENAME, 'w', encoding="utf-8") as fl:
        for emp in tasks:
            fl.write(str(emp)+"\n")

def add_tasks(tasks, task):
    tasks.append(task)
    return tasks
def print_base(tasks):
    for person in tasks:
        print(person)
try:
    tasks = load_tasks(FILENAME)
except:
    tasks = []

while True:
    sw = input("1 - save base in file, 2 - add task, 3 - print, 0 - exit.")
    if sw == '1':
        save_tasks(tasks)
    elif sw == '2':
        print("Enter new info:")
        name = input("Name: ")
        age = input("Age: ")
        task = {'name': name, 'age': age}
        add_tasks(tasks, task)
    elif sw == '3':
        print_base(tasks)
    elif sw == '0':
        break
