# Teste l'enregistrement et le chargement de la liste de tâches

from json import loads
import pytest
from src.models.Task import Task
from src.models.TaskList import TaskList


def test_load_from_empty_file():
    task_list = TaskList()
    task_list.load_from_file("tests/fixtures/empty_valid.json")
    assert len(task_list.get_tasks()) == 0

def test_load_from_invalid_file():
    task_list = TaskList()
    with pytest.raises(ValueError) as e:
        task_list.load_from_file("tests/fixtures/invalid.json")

def test_load_all_tasks_with_task():
    task_list = TaskList()
    task_list.load_from_file("tests/fixtures/containing_task.json")
    assert len(task_list.get_tasks()) == 1  

def test_load_all_tasks_with_tasks():
    task_list = TaskList()
    task_list.load_from_file("tests/fixtures/containing_tasks.json")
    assert len(task_list.get_tasks()) == 4

def test_load_taks_with_all_attributes():
    task_list = TaskList()
    task_list.load_from_file("tests/fixtures/containing_tasks.json")
    assert task_list.get_tasks()[0].get_name() == "test 1"
    assert task_list.get_tasks()[0].get_description() == "description test 1"
    assert task_list.get_tasks()[0].is_done() == False

    assert task_list.get_tasks()[1].get_name() == "test 2"
    assert task_list.get_tasks()[1].get_description() == "description test 2"
    assert task_list.get_tasks()[1].is_done() == False

def test_save_tak():
    task_list = TaskList()
    task1 = Task("test 1", "description test 1")
    task2 = Task("test 2", "description test 2")
    task_list.add_task(task1)
    task_list.add_task(task2)
    task_list.save_to_file("tests/tmp/save.json")
    content = loads(open("tests/tmp/save.json", "r").read())
    assert content[0]["name"] == "test 1"
    assert content[0]["description"] == "description test 1"
    assert content[1]["name"] == "test 2"
    assert content[1]["description"] == "description test 2"