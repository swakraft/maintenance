from src.models.Task import Task
from src.models.TaskList import TaskList


def test_add_task():
    task_list = TaskList()
    task_list.add_task(Task("test 1", "description test 1"))
    assert len(task_list.get_tasks()) == 1

def test_remove_task():
    task_list = TaskList()
    task_list.add_task(Task("test 1", "description test 1"))
    task_list.remove_task(Task("test 1", "description test 1"))
    assert len(task_list.get_tasks()) == 0