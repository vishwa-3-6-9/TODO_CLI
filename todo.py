tasks = []

def show_menu():
    print("\n---TO-DO APP---")
    print("1.View Tasks")
    print("2.Add Task")
    print("3.Remove Task")
    print("4.Exit")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\n Your Task:")
        for index,task in enumerate(tasks,start = 1):
            print(f"{index}.{task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        task_number = int(input("Enter task number to remove:"))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid choice.try again.")

