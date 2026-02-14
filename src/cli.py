from src.models.Task import Task
from src.models.TaskList import TaskList

DATA_FILE = "tasks.json"


def display_menu():
    print("\n--- Task Manager Light ---")
    print("1. Lister les tâches")
    print("2. Ajouter une tâche")
    print("3. Marquer une tâche comme terminée")
    print("4. Marquer une tâche comme non terminée")
    print("5. Supprimer une tâche")
    print("6. Sauvegarder")
    print("7. Charger")
    print("8. Quitter")


def display_tasks(task_list: TaskList):
    tasks = task_list.get_tasks()
    if not tasks:
        print("Aucune tâche.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task.is_done() else " "
        print(f"  {i}. [{status}] {task.get_name()} - {task.get_description()}")


def select_task(task_list: TaskList) -> Task | None:
    tasks = task_list.get_tasks()
    if not tasks:
        print("Aucune tâche.")
        return None
    display_tasks(task_list)
    try:
        index = int(input("Numéro de la tâche : ")) - 1
        return tasks[index]
    except (ValueError, IndexError):
        print("Sélection invalide.")
        return None


def main():
    task_list = TaskList()

    while True:
        display_menu()
        choice = input("Choix : ").strip()

        if choice == "1":
            display_tasks(task_list)

        elif choice == "2":
            name = input("Nom : ").strip()
            description = input("Description : ").strip()
            task_list.add_task(Task(name, description))
            print(f"Tâche '{name}' ajoutée.")

        elif choice == "3":
            task = select_task(task_list)
            if task:
                task.mark_done()
                print(f"Tâche '{task.get_name()}' marquée comme terminée.")

        elif choice == "4":
            task = select_task(task_list)
            if task:
                task.mark_undone()
                print(f"Tâche '{task.get_name()}' marquée comme non terminée.")

        elif choice == "5":
            task = select_task(task_list)
            if task:
                task_list.remove_task(task)
                print(f"Tâche '{task.get_name()}' supprimée.")

        elif choice == "6":
            task_list.save_to_file(DATA_FILE)
            print(f"Sauvegardé dans {DATA_FILE}.")

        elif choice == "7":
            task_list.load_from_file(DATA_FILE)
            print(f"Chargé depuis {DATA_FILE}.")

        elif choice == "8":
            print("Au revoir.")
            break

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
