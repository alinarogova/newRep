FILENAME = 'tasks.txt'
def load_tasks(FILENAME):
    tasks = []
    with open(FILENAME, 'r', encoding="utf-8") as fl:
        for line in fl.readlines():
            tasks.append(line.split())

def save_tasks(tasks):
    with open(FILENAME, 'w', encoding="utf-8"):
        pass

def add_tasks(tasks, task):
