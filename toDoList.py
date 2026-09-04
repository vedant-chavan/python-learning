task = ["python", "laravel", "java", "go", "php"]

def show(task):
    if not task:
        print("no task added till now. Add some Task to view")
    else:
        for index, values in enumerate(task , start = 1):
            print(f"{index} . {values}")

def add(task):
    newTask = input("Enter Task You Want To Add : ")
    task.append(newTask)
    print("Task Added successfully")

def update(task):
    update_number = int(input("Enter task number"))
    updated_task = input("Enter new task")
    length_task = len(task)
    if(length_task >= update_number and update_number > 0):
        task[update_number - 1] = updated_task
        print("task update successfully")
    else:
        print("Invalid task number")

def delete(task):
    task_number = int(input("Enter the task number : "))
    task_length = len(task)

    if(task_number <= task_length and task_number > 0):
        task.pop(task_number-1)
        print("Task deleted successfully")
        show(task)
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

        if(choice == 2):
            add(task)
        elif(choice == 1):
            show(task)
        elif(choice == 3):
            update(task)
        elif(choice == 4):
            delete(task)
        elif(choice == 5):
            print("bye bye")
            break
        else:
            print("Invalid Input")
    except IndexError as e:
        print("Invalid Input")
    except ValueError as e:
        print("Invalid Input")



