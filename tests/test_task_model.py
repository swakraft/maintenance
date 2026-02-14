

from src.models.Task import Task


def test_crate_task_deault_values():
    task = Task("test 1", "description test 1")
    assert task.get_name() == "test 1"
    assert task.get_description() == "description test 1"
    assert task.is_done() == False

def test_mark_as_done():
    task = Task("test 1", "description test 1")
    task.mark_done()
    assert task.is_done() == True

def test_mark_undone():
    task = Task("test 1", "description test 1")
    task.mark_done()
    assert task.is_done() == True
    task.mark_undone()
    assert task.is_done() == False

def test_edit_field_description():
    task = Task("test 1", "description test 1")
    task.set_description("description test 2")
    assert task.get_description() == "description test 2"

def test_edit_field_name():
    task = Task("test 1", "description test 1")
    task.set_name("test 2")
    assert task.get_name() == "test 2"