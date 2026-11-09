# Day 9: Mini Project - Persistent Task Assistant (OOPs version)
import json

class TaskManager:

    def __init__(self):
        self.file_name = "tasks.json"
        self.tasks = []

    # Add task
    def add_task(self):

        print("\n=== Add a new task ===")

        task_name = input("Enter a new task: ")

        if not task_name.strip():
            print("Error: Task name cannot be empty.")
            return

        self.tasks.append({
            "task": task_name,
            "completed": False
        })

        self.save_tasks()

        print("Task added successfully!")

    # Display tasks
    def display_tasks(self):

        print("\n=== All tasks ===")

        if not self.tasks:
            print("No tasks available.")
            return

        for i, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['task']} - [{status}]")

    # Mark task as completed
    def mark_task_complete(self):

        print("\n=== Mark a task as complete ===")

        if not self.tasks:
            print("No tasks available to complete.")
            return

        self.display_tasks()

        try:

            task_id = int(input("Enter a task ID to mark as complete: "))

            if task_id < 1 or task_id > len(self.tasks):
                print("Invalid task ID. Please enter a number between 1 and", len(self.tasks))
                return

            task = self.tasks[task_id - 1]

            if task["completed"]:
                print("This task is already completed.")
                return

            task["completed"] = True
            self.save_tasks()
            print("Task marked as complete!")

        except ValueError:
            print("Error: Please enter a valid number.")

    # Delete task
    def delete_task(self):

        print("\n=== Delete a task ===")

        # 1. Check if tasks are empty
        if not self.tasks:
            print("No tasks available to delete.")
            return

        # 2. Display tasks
        self.display_tasks()

        try:

            # 3. Ask for task ID
            task_id = int(input("Enter a task ID to delete: "))

            # 4. Validate task ID
            if not 1 <= task_id <= len(self.tasks):
                print("Invalid task ID. Please enter a number between 1 and", len(self.tasks))
                return

            # 5. Delete the task
            deleted_task = self.tasks.pop(task_id - 1)
            self.save_tasks()
            print(f"Task '{deleted_task['task']}' deleted successfully!")

        except ValueError:
            print("Error: Please enter a valid number.")

    # Save tasks
    def save_tasks(self):

        print("\n=== Save all tasks ===")

        with open(self.file_name, "w") as file:
            json.dump(self.tasks, file, indent=4)
        print("Tasks saved successfully!")

    # load tasks
    def load_tasks(self):

        print("\n=== Load all tasks ===")

        try:
            with open(self.file_name, "r") as file:
                self.tasks = json.load(file)
                print("Tasks loaded successfully!")

        except FileNotFoundError:
            self.tasks = []
            print("No saved tasks found. Starting with an empty list.")

        except json.JSONDecodeError:
            print("Error: The tasks file contains invalid JSON.")
            print("The existing file has not been modified.")

    # Main program
    def run(self):
        self.load_tasks()

        print("=== Persistent Task Assistant ===")
        name = input("What is your name? ").strip()

        if not name:
            name = "Guest"
            print("Using default name:", name)

        running = True
        while running:
            print("\n=== Menu ===")
            print("1. Add a new task")
            print("2. Mark a task as complete")
            print("3. Display all tasks")
            print("4. Delete a task")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.mark_task_complete()
            elif choice == "3":
                self.display_tasks()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                running = False
                print("Exiting the program...")
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        print("\n=== Your Saved Tasks ===")
        self.display_tasks()

        print(f"\nThank you, {name}!")

if __name__ == '__main__':
    # Create a TaskManager object
    manager = TaskManager()

    # Testing check-in
    manager.run()

