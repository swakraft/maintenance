# Diagramme de classes

```plantuml
class Task {
	- __name: str
	- __description: str
	- __done: bool

	+ mark_done()
	+ mark_undone()
	+ is_done(): bool
	+ get_name(): str
	+ get_description(): str
	+ set_name(name: str)
	+ set_description(description: str)
	+ to_json(): dict
	+ __eq__(value: object): bool
	+ __str__(): str
	+ __repr__(): str
}

class TaskList {
	- __tasks: list[Task]

	+ add_task(task: Task)
	+ remove_task(task: Task)
	+ get_tasks(): list[Task]
	+ clear_tasks()
	+ save_to_file(path: str)
	+ load_from_file(path: str)
}

TaskList "1" *-- "0..*" Task : contient
```