from json import dumps, loads

from src.models.Task import Task


class TaskList:
    def __init__(self):
        self.__tasks: list[Task] = []

    def add_task(self, task):
        self.__tasks.append(task)
    
    def get_tasks(self):
        return self.__tasks
    
    def remove_task(self, task):
        self.__tasks.remove(task)

    def clear_tasks(self):
        self.__tasks = []
    
    def save_to_file(self, path: str):
        open(path, "w").write(dumps([task.to_json() for task in self.__tasks]))

    def load_from_file(self, path: str):
        self.__tasks = [Task(name = task["name"], description = task["description"]) for task in loads(open(path, "r").read())]