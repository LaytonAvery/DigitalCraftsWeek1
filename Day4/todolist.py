
choice = ""
task = {}


def add_task(choice):
    task = [{"title": name, "priority": priority}]
    task.append("")
    for key, value in task.append(""):
        print(key, value)
    # print(task)


def delete_task(choice):
    del task


def view_all():
    for key, value in task.items():
        print(key, value)


choice = input("""
    Welcome to your TODO app!
    Press 1 to 'Add Task'.
    Press 2 to 'Delete Task'.
    Press 3 to 'View All Tasks'.
    Press q to QUIT.""")
print(choice)


while True:
    choice = input("""
    Welcome to your TODO app!
    Press 1 to 'Add Task'.
    Press 2 to 'Delete Task'.
    Press 3 to 'View All Tasks'.
    Press q to QUIT.""")
print(choice)

   if choice == "1":
        name = input("Enter a task: ")
        priority = input("Enter task priority: ")
        add_task(choice)

    elif choice == "2":
        for items in task():
            print(items)
            deletion = input("What would you like deleted? ")
            delete_task(choice)

    elif choice == "3":
        view_all()

    elif choice == "q":
        break
