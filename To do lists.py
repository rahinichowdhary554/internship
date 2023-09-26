tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index+1}. {task}")

def update_task():
    view_tasks()
    task_index = int(input("Enter the task number to update: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
    else:
        new_task = input("Enter the updated task: ")
        tasks[task_index] = new_task
        print("Task updated successfully!")

def delete_task():
    view_tasks()
    task_index = int(input("Enter the task number to delete: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
    else:
        del tasks[task_index]
        print("Task deleted successfully!")

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
