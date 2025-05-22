import os

TASK_FILE = "d:/python-beginners-projects/to_do_list/tasks.txt"

def load_task():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]
    
def save_task(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_task(tasks):
    if not tasks:
        print("No tasks found")
    else:
        for i, task in enumerate(tasks,start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task : ")
    tasks = load_task()
    tasks.append(f"[]{task}")
    save_task(tasks)
    print("Task added.")

def mark_task_done():
    tasks = load_task()
    display_task(tasks)
    try:
        num = int(input("Enter a task number to mark as done : "))
        if 1 <= num <= len(tasks):
            tasks[num-1] = tasks[num-1].replace("[]","[x]")
            save_task(tasks)
            print("Task marked as done")
        else:
            print("Invalid task number")
    except ValueError:
        print("Enter a valid number")

def delete_task():
    tasks = load_task()
    display_task(tasks)
    try:
        num = int(input("Enter task number to delete : "))
        if 1 <= num <= len(tasks):
            deleted = tasks.pop(num-1)
            save_task(tasks)
            print(f"Deleted Task : {deleted}")
        else:
            print("Invalid number")
    except ValueError:
        print("Enter a valid number.")

def main():
    while True:
        print("\n==== TO_DO_LIST ====")
        print("1. View tasks")
        print("2. Add tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Choose an option : ")

        if choice == '5':
            print("Thanks for using it!")
            break

        if choice == '1':
            display_task(load_task())
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_task_done()
        elif choice == '4':
            delete_task()
        else:
            print("Invalid choice. Please enter 1-5.")
        
if __name__ == "__main__":
    main()