import json
import os
import uuid
from datetime import datetime

# --- Global Variables ---
TASKS_FILE = 'tasks.json'
tasks = [] # This will store our list of task dictionaries

# --- Helper Functions ---

def load_tasks():
    """Loads tasks from the TASKS_FILE. If the file doesn't exist, initializes an empty list."""
    global tasks
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as f:
                tasks = json.load(f)
            print(f"Loaded {len(tasks)} tasks from {TASKS_FILE}.")
        except json.JSONDecodeError:
            print(f"Error reading {TASKS_FILE}. Starting with an empty list.")
            tasks = []
        except Exception as e:
            print(f"An unexpected error occurred while loading tasks: {e}. Starting with an empty list.")
            tasks = []
    else:
        print("No existing tasks file found. Starting with an empty list.")
        tasks = []

def save_tasks():
    """Saves the current tasks list to the TASKS_FILE."""
    try:
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=4)
        print(f"Saved {len(tasks)} tasks to {TASKS_FILE}.")
    except Exception as e:
        print(f"Error saving tasks to {TASKS_FILE}: {e}")

def get_task_by_id(task_id):
    """Finds and returns a task dictionary by its ID."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def get_task_description_by_id(task_id):
    """Returns the description of a task given its ID."""
    task = get_task_by_id(task_id)
    return task["description"] if task else "Unknown Task"

def get_task_id_by_description(description):
    """Returns the ID of the first task found with a given description."""
    for task in tasks:
        if task["description"].lower() == description.lower():
            return task["id"]
    return None

# --- Main Application Functions ---

def display_menu():
    """Prints the main menu options to the console."""
    print("\n--- To-Do List Application Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Edit Task")
    print("5. Search Tasks")
    print("6. Manage Subtasks")
    print("7. Manage Dependencies")
    print("8. Exit")
    print("-----------------------------------")

def add_task():
    """Prompts the user for task details and adds a new task to the list."""
    print("\n--- Add New Task ---")
    description = input("Enter task description: ").strip()
    if not description:
        print("Task description cannot be empty. Task not added.")
        return

    priority_options = ["High", "Medium", "Low"]
    priority = ""
    while priority not in priority_options:
        priority = input(f"Enter priority ({'/'.join(priority_options)}): ").strip().capitalize()
        if priority not in priority_options:
            print("Invalid priority. Please choose from High, Medium, or Low.")

    categories_input = input("Enter categories (comma-separated, e.g., Work, Personal): ").strip()
    categories = [cat.strip() for cat in categories_input.split(',') if cat.strip()]

    due_date = input("Enter due date (YYYY-MM-DD, leave blank if none): ").strip()
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Due date not set.")
            due_date = ""

    new_task = {
        "id": str(uuid.uuid4()), # Generate a unique ID for the task
        "description": description,
        "priority": priority,
        "categories": categories,
        "due_date": due_date,
        "is_complete": False,
        "dependencies": [], # List of task IDs that this task depends on
        "subtasks": [] # List of subtask dictionaries
    }
    tasks.append(new_task)
    print("Task added successfully!")

def view_tasks():
    """Displays all tasks, optionally grouped/filtered."""
    if not tasks:
        print("\nYour to-do list is empty!")
        return

    print("\n--- Your To-Do List ---")
    print("1. View All Tasks")
    print("2. View Incomplete Tasks")
    print("3. View Complete Tasks")
    print("4. View by Category")
    print("5. View by Priority")
    print("6. View by Due Date (Upcoming)")
    print("-----------------------")
    choice = input("Enter your viewing choice: ").strip()

    filtered_tasks = []
    today = datetime.now().date()

    if choice == '1':
        filtered_tasks = tasks
    elif choice == '2':
        filtered_tasks = [task for task in tasks if not task["is_complete"]]
    elif choice == '3':
        filtered_tasks = [task for task in tasks if task["is_complete"]]
    elif choice == '4':
        category_filter = input("Enter category to filter by: ").strip()
        filtered_tasks = [task for task in tasks if category_filter.lower() in [c.lower() for c in task["categories"]]]
    elif choice == '5':
        priority_filter = input("Enter priority to filter by (High/Medium/Low): ").strip().capitalize()
        filtered_tasks = [task for task in tasks if task["priority"] == priority_filter]
    elif choice == '6':
        # Sort tasks by due date for upcoming view
        upcoming_tasks = [task for task in tasks if task["due_date"] and not task["is_complete"]]
        # Filter for tasks with a valid due date that is today or in the future
        upcoming_tasks = [task for task in upcoming_tasks if datetime.strptime(task["due_date"], "%Y-%m-%d").date() >= today]
        filtered_tasks = sorted(upcoming_tasks, key=lambda x: datetime.strptime(x["due_date"], "%Y-%m-%d"))
    else:
        print("Invalid viewing choice.")
        return

    if not filtered_tasks:
        print("No tasks found matching your criteria.")
        return

    # Sort tasks by completion status, then priority, then due date
    filtered_tasks.sort(key=lambda x: (x["is_complete"],
                                        {"High": 0, "Medium": 1, "Low": 2}.get(x["priority"], 99),
                                        x["due_date"] if x["due_date"] else "9999-12-31"))

    for i, task in enumerate(filtered_tasks):
        status = "[COMPLETED]" if task["is_complete"] else "[PENDING]"
        categories_str = f" ({', '.join(task['categories'])})" if task["categories"] else ""
        due_date_str = f" (Due: {task['due_date']})" if task["due_date"] else ""
        print(f"\n{i+1}. {status} [ID: {task['id'][:8]}] {task['description']} [Priority: {task['priority']}] {categories_str}{due_date_str}")

        # Display dependencies
        if task["dependencies"]:
            dep_descriptions = [get_task_description_by_id(dep_id) for dep_id in task["dependencies"]]
            print(f"    Depends on: {', '.join(dep_descriptions)}")

        # Display subtasks
        if task["subtasks"]:
            print("    Subtasks:")
            for sub_i, subtask in enumerate(task["subtasks"]):
                sub_status = "[DONE]" if subtask["is_complete"] else "[TODO]"
                print(f"        {sub_i+1}. {sub_status} {subtask['description']}")
    print("-----------------------")


def mark_complete():
    """Marks a task as complete if its dependencies are met."""
    print("\n--- Mark Task as Complete ---")
    if not tasks:
        print("No tasks to mark complete.")
        return

    task_id_to_complete = input("Enter the ID of the task to mark as complete: ").strip()
    task = get_task_by_id(task_id_to_complete)

    if not task:
        print("Task not found.")
        return

    if task["is_complete"]:
        print(f"Task '{task['description']}' is already complete.")
        return

    # Check dependencies
    pending_dependencies = [
        get_task_description_by_id(dep_id) for dep_id in task["dependencies"]
        if get_task_by_id(dep_id) and not get_task_by_id(dep_id)["is_complete"]
    ]

    if pending_dependencies:
        print(f"Cannot complete '{task['description']}'. The following dependencies are not yet complete:")
        for dep_desc in pending_dependencies:
            print(f"- {dep_desc}")
        return

    task["is_complete"] = True
    print(f"Task '{task['description']}' marked as complete!")

def edit_task():
    """Allows the user to edit an existing task's details."""
    print("\n--- Edit Task ---")
    if not tasks:
        print("No tasks to edit.")
        return

    task_id_to_edit = input("Enter the ID of the task to edit: ").strip()
    task = get_task_by_id(task_id_to_edit)

    if not task:
        print("Task not found.")
        return

    print(f"Editing task: '{task['description']}'")
    print("Leave field blank to keep current value.")

    new_description = input(f"New description (current: {task['description']}): ").strip()
    if new_description:
        task["description"] = new_description

    priority_options = ["High", "Medium", "Low"]
    new_priority = input(f"New priority ({'/'.join(priority_options)}, current: {task['priority']}): ").strip().capitalize()
    if new_priority and new_priority in priority_options:
        task["priority"] = new_priority
    elif new_priority:
        print("Invalid priority provided. Keeping current priority.")

    new_categories_input = input(f"New categories (comma-separated, current: {', '.join(task['categories'])}): ").strip()
    if new_categories_input:
        task["categories"] = [cat.strip() for cat in new_categories_input.split(',') if cat.strip()]

    new_due_date = input(f"New due date (YYYY-MM-DD, current: {task['due_date'] if task['due_date'] else 'None'}): ").strip()
    if new_due_date:
        try:
            datetime.strptime(new_due_date, "%Y-%m-%d")
            task["due_date"] = new_due_date
        except ValueError:
            print("Invalid date format. Keeping current due date.")
    elif new_due_date == "": # Allow clearing due date
        task["due_date"] = ""

    print("Task updated successfully!")

def search_tasks():
    """Searches for tasks by keyword, category, or due date."""
    print("\n--- Search Tasks ---")
    if not tasks:
        print("No tasks to search.")
        return

    print("Search by:")
    print("1. Keyword (in description)")
    print("2. Category")
    print("3. Due Date")
    search_choice = input("Enter your search choice: ").strip()

    search_results = []
    if search_choice == '1':
        keyword = input("Enter keyword to search: ").strip().lower()
        search_results = [task for task in tasks if keyword in task["description"].lower()]
    elif search_choice == '2':
        category = input("Enter category to search: ").strip().lower()
        search_results = [task for task in tasks if category in [c.lower() for c in task["categories"]]]
    elif search_choice == '3':
        due_date_str = input("Enter due date (YYYY-MM-DD) to search: ").strip()
        search_results = [task for task in tasks if task["due_date"] == due_date_str]
    else:
        print("Invalid search choice.")
        return

    if not search_results:
        print("No tasks found matching your search criteria.")
        return

    print("\n--- Search Results ---")
    for i, task in enumerate(search_results):
        status = "[COMPLETED]" if task["is_complete"] else "[PENDING]"
        categories_str = f" ({', '.join(task['categories'])})" if task["categories"] else ""
        due_date_str = f" (Due: {task['due_date']})" if task["due_date"] else ""
        print(f"{i+1}. {status} [ID: {task['id'][:8]}] {task['description']} [Priority: {task['priority']}] {categories_str}{due_date_str}")
    print("-----------------------")

def manage_subtasks():
    """Manages subtasks for a given parent task."""
    print("\n--- Manage Subtasks ---")
    if not tasks:
        print("No tasks to manage subtasks for.")
        return

    task_id = input("Enter the ID of the parent task: ").strip()
    parent_task = get_task_by_id(task_id)

    if not parent_task:
        print("Parent task not found.")
        return

    while True:
        print(f"\n--- Subtasks for '{parent_task['description']}' ---")
        if not parent_task["subtasks"]:
            print("No subtasks yet.")
        else:
            for i, subtask in enumerate(parent_task["subtasks"]):
                status = "[DONE]" if subtask["is_complete"] else "[TODO]"
                print(f"{i+1}. {status} {subtask['description']}")

        print("\nSubtask Options:")
        print("1. Add Subtask")
        print("2. Mark Subtask as Complete")
        print("3. Back to Main Menu")
        sub_choice = input("Enter your choice: ").strip()

        if sub_choice == '1':
            sub_description = input("Enter subtask description: ").strip()
            if sub_description:
                parent_task["subtasks"].append({"id": str(uuid.uuid4()), "description": sub_description, "is_complete": False})
                print("Subtask added.")
            else:
                print("Subtask description cannot be empty.")
        elif sub_choice == '2':
            if not parent_task["subtasks"]:
                print("No subtasks to mark complete.")
                continue
            try:
                sub_index = int(input("Enter the number of the subtask to mark complete: ")) - 1
                if 0 <= sub_index < len(parent_task["subtasks"]):
                    parent_task["subtasks"][sub_index]["is_complete"] = True
                    print("Subtask marked complete.")
                else:
                    print("Invalid subtask number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif sub_choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_dependencies():
    """Allows adding dependencies between tasks."""
    print("\n--- Manage Dependencies ---")
    if len(tasks) < 2:
        print("You need at least two tasks to set up dependencies.")
        return

    print("Existing Tasks (for reference):")
    for task in tasks:
        print(f"- [ID: {task['id'][:8]}] {task['description']}")

    task_id = input("Enter the ID of the task that will have a dependency: ").strip()
    dependent_task = get_task_by_id(task_id)

    if not dependent_task:
        print("Task not found.")
        return

    dependency_id = input("Enter the ID of the task that MUST be completed BEFORE this one: ").strip()
    prerequisite_task = get_task_by_id(dependency_id)

    if not prerequisite_task:
        print("Prerequisite task not found.")
        return

    if dependent_task["id"] == prerequisite_task["id"]:
        print("A task cannot depend on itself.")
        return

    if prerequisite_task["id"] in dependent_task["dependencies"]:
        print(f"Task '{dependent_task['description']}' already depends on '{prerequisite_task['description']}'.")
        return

    # Optional: Implement a check for circular dependencies if time allows.
    # For now, we assume users will not create circular dependencies.

    dependent_task["dependencies"].append(prerequisite_task["id"])
    print(f"Dependency added: Task '{dependent_task['description']}' now depends on '{prerequisite_task['description']}'.")

def check_reminders():
    """Checks for tasks due today and prints reminders."""
    today = datetime.now().strftime("%Y-%m-%d")
    reminders = [task for task in tasks if task["due_date"] == today and not task["is_complete"]]
    if reminders:
        print("\n--- REMINDERS (Due Today!) ---")
        for task in reminders:
            print(f"- [ID: {task['id'][:8]}] {task['description']} (Priority: {task['priority']})")
        print("-------------------------------")

# --- Main Application Loop ---

def main():
    """The main function to run the to-do list application."""
    load_tasks()
    check_reminders()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_complete()
        elif choice == '4':
            edit_task()
        elif choice == '5':
            search_tasks()
        elif choice == '6':
            manage_subtasks()
        elif choice == '7':
            manage_dependencies()
        elif choice == '8':
            save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
