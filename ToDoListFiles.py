import json

file_name = "to_do_task_file.json"

def load_file():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File Not Found")
        return []
    except json.JSONDecodeError:
        print("File is empty! Add Data First To View list")
        return []

task_list = load_file()

def save_file(task_list):
    with open(file_name, "w") as file:
        json.dump(task_list,file)

def show_task(task):
    if not task:
        print("no task added till now. Add some Task to view")
    else:
        for index, values in enumerate(task , start = 1):
            print(f"{index} . {values}")

def add_task(task_list):
    newTask = input("Enter Task You Want To Add : ")
    task_list.append(newTask)
    save_file(task_list)
    print("Task Added successfully")

def update_task(task_list):
    update_number = int(input("Enter task number : "))
    updated_task = input("Enter new task : ")
    length_task = len(task_list)
    if(length_task >= update_number and update_number > 0):
        task_list[update_number - 1] = updated_task
        save_file(task_list)
        print("task update successfully")
    else:
        print("Invalid task number")

def delete_task(task_list):
    task_number = int(input("Enter the task number : "))
    task_length = len(task_list)

    if(task_number <= task_length and task_number > 0):
        task_list.pop(task_number-1)
        save_file(task_list)
        print("Task deleted successfully")
    else:
        print("Task not found. Enter Valid Task number")

while True:
    try:
        choice = int(input(""" ********* To Do Task *********
        1.View Tasks 
        2.Add Task 
        3.Update task
        4.Delete Task
        5.Exit
        Enter your Choise : """))

        if(choice == 1):
            show_task(task_list)
        elif(choice == 2):
            add_task(task_list)
        elif(choice == 3):
            update_task(task_list)
        elif(choice == 4):
            delete_task(task_list)
        elif(choice == 5):
            break
        else:
            print("Invalid Input")
    except IndexError as e:
        print("Invalid Input")
    except ValueError as e:
        print("Invalid Input")
    except FileNotFoundError:
        print("File Not Found")
