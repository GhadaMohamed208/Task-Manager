"""
Task Manager System
--------------------
A simple console-based task management application.

Client   : TechMaster Academy
Project  : Task Manager System
Storage  : tasks.json (no database required)

Features:
    - Add a new task
    - View all tasks
    - Update an existing task
    - Delete a task
    - Mark a task as completed

Each task is stored as a dictionary:
    {"id": 1, "title": "Study Python", "completed": False}

All tasks together are stored as a list of dictionaries, and that list
is what gets saved to / loaded from tasks.json so tasks survive a
restart of the program.
"""

import json

TASKS_FILE = "tasks.json"


# ---------------------------------------------------------------------
# FILE HANDLING (load_tasks / save_tasks)
# ---------------------------------------------------------------------

def load_tasks(filename=TASKS_FILE):
    """Read tasks.json into memory and return a list of task dicts.

    If the file doesn't exist yet (very first run) or contains invalid
    JSON, the app starts fresh with an empty list instead of crashing.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    except json.JSONDecodeError:
        print("Warning: tasks.json was corrupted or empty. Starting fresh.")
        tasks = []
    else:
        print("Tasks loaded.")
    return tasks


def save_tasks(tasks, filename=TASKS_FILE):
    """Write the tasks list back to tasks.json, neatly formatted."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


# ---------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------

def find_task(tasks, task_id):
    """Return the task dict with the given id, or None if not found."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def next_task_id(tasks):
    """Generate the next unique id: one more than the highest existing id."""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def prompt_task_id(tasks, prompt="Task ID: "):
    """Ask the user for a task id, validating that it's a number and
    that a task with that id actually exists. Returns None on failure
    so the calling function can bail out cleanly.
    """
    try:
        task_id = int(input(prompt))
    except ValueError:
        print("Please enter a valid whole number for the ID.")
        return None

    task = find_task(tasks, task_id)
    if task is None:
        print(f"No task with ID {task_id} was found.")
        return None

    return task_id


# ---------------------------------------------------------------------
# CORE FEATURES
# ---------------------------------------------------------------------

def add_task(tasks):
    """Create a new task and append it to the tasks list."""
    title = input("Title: ").strip()
    if not title:
        print("Title cannot be empty. Task was not added.")
        return

    task = {
        "id": next_task_id(tasks),
        "title": title,
        "completed": False,
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added with ID {task['id']}.")


def view_tasks(tasks):
    """Print every current task."""
    if not tasks:
        print("No tasks yet. Add one from the main menu!")
        return

    print("\n{:<5}{:<10}{}".format("ID", "Status", "Title"))
    print("-" * 40)
    for task in tasks:
        status = "Done" if task["completed"] else "Pending"
        print("{:<5}{:<10}{}".format(task["id"], status, task["title"]))
    print()


def update_task(tasks):
    """Edit the title of an existing task."""
    if not tasks:
        print("There are no tasks to update yet.")
        return

    task_id = prompt_task_id(tasks, "ID of task to update: ")
    if task_id is None:
        return

    task = find_task(tasks, task_id)
    new_title = input("New title: ").strip()
    if not new_title:
        print("Title cannot be empty. Task was not updated.")
        return

    task["title"] = new_title
    save_tasks(tasks)
    print(f"Task {task_id} updated.")


def delete_task(tasks):
    """Remove a task from the list."""
    if not tasks:
        print("There are no tasks to delete yet.")
        return

    task_id = prompt_task_id(tasks, "ID of task to delete: ")
    if task_id is None:
        return

    task = find_task(tasks, task_id)
    tasks.remove(task)
    save_tasks(tasks)
    print(f"Task {task_id} deleted.")


def complete_task(tasks):
    """Mark an existing task as completed."""
    if not tasks:
        print("There are no tasks to complete yet.")
        return

    task_id = prompt_task_id(tasks, "ID of task to mark as completed: ")
    if task_id is None:
        return

    task = find_task(tasks, task_id)
    if task["completed"]:
        print("Already done.")
        return

    task["completed"] = True
    save_tasks(tasks)
    print(f"Task {task_id} marked as completed.")


# ---------------------------------------------------------------------
# MENU / MAIN LOOP
# ---------------------------------------------------------------------

def display_menu():
    print("\n===== TASK MANAGER =====")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")


def main():
    tasks = load_tasks()
    running = True

    while running:
        display_menu()
        choice = input("> ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            complete_task(tasks)
        elif choice == "6":
            print("Goodbye!")
            running = False
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()
