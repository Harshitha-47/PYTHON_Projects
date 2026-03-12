# -------------------------------------------------------------
# Task Scheduler System
# This Python program simulates a basic task scheduling system.
# Users can add tasks, view scheduled tasks, and mark tasks as
# completed. Each task maintains a status such as Pending or
# Completed. The program demonstrates simple task management
# similar to operating system scheduling concepts.
# -------------------------------------------------------------

tasks = []

def add_task():
    task_name = input("Enter task name: ")
    tasks.append({"task": task_name, "status": "Pending"})
    print("Task added successfully.\n")


def view_tasks():
    print("\n========== TASK LIST ==========")

    if len(tasks) == 0:
        print("No tasks available.")
    else:
        for i in range(len(tasks)):
            task = tasks[i]
            print(f"{i+1}. {task['task']}  -->  {task['status']}")

    print("================================\n")


def complete_task():
    view_tasks()

    try:
        task_number = int(input("Enter task number to mark as completed: "))
        tasks[task_number - 1]["status"] = "Completed"
        print("Task marked as completed.\n")
    except:
        print("Invalid task number.\n")


def main():

    while True:

        print("========= TASK SCHEDULER =========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            print("Exiting Task Scheduler...")
            break

        else:
            print("Invalid choice. Please try again.\n")


main()