print("TO-DO-LIST")
print("KEEP YOUR TASKS REMINDED FROM HERE")
print("Enter 'ADD' to add tasks")
print("Enter 'UPDATE' to update tasks") 
print("Enter 'DELETE' to delete tasks")
print("Enter 'VIEW' to view tasks")
print("Enter 'PENDING' to pending tasks")
print("Enter 'COMPLETED' to completed tasks")
print("Enter 'MARK' to mark completed tasks")
print("Enter 'EXIT' to exit")
Tasks=[]
while True:
    option=input('Enter your option: ').upper()
    if option == 'ADD':
        task_title = input("Add a new task: ")
        task = {"title" : task_title, "status" : "PENDING"}
        Tasks.append(task)
        print('Task added!')
    elif option =='UPDATE':
        if not Tasks:
            print("No tasks to be updated")
        else:
            print("Current tasks: ")
            for i in range(len(Tasks)):
                 t = Tasks[i]
                 print(f"Task {i} - {t['title']}, Status : {t['status']}")
            try:
                task_number=int(input(" Enter the task number to be updated (Task number starts from 0): "))
                if 0<=task_number<len(Tasks):
                    updated_task=input("Enter a new task: ")
                    Tasks[task_number]['title']=updated_task
                    print('Task updated sucessfully!!')
                else:
                    print("Invalid task number") 
            except ValueError:
                print("Enter a valid number: ")

    elif option == 'DELETE':
        if not Tasks:
            print("No tasks to be deleted")
        else:
             print("Current tasks: ")
             for i in range(len(Tasks)):
                t = Tasks[i]
                print(f"Task {i} - {t['title']}, Status : {t['status']}")
             try:
                task_number=int(input(" Enter the task number to be deleted (Task number starts from 0): "))
                if 0<=task_number<len(Tasks):
                    deleted_task=Tasks.pop(task_number)
                    print("Deleted task : {deleted_task['title']} successfully!!")
                else:
                    print("Invalid task number")
             except ValueError:
                print("Enter a valid number: ")

    elif option == 'PENDING':
        found = False
        print("Pending Tasks")
        for task in Tasks:
            if task['status'] == 'PENDING':
                print(f" - {task['title']}")
                found = True
            if not found:
                print("No pending tasks")

    elif option == 'COMPLETED':
            print("Completed Tasks")
            has_completed =False
            for task in Tasks:
                if task['status'] == 'COMPLETED':
                    print(f" - {task['title']}")
                    has_completed = True
                if not has_completed:
                    print("No completed tasks")
    elif option == 'MARK':
            if not Tasks:
                print("No tasks to mark as completed.")
            else:
                print("Current status of tasks:")
                for i  in range(len(Tasks)):
                    t = Tasks[i]
                    print(f"Task {i} - {t['title']}, Status: {t['status']}")
                try:
                    task_number = int(input("Enter the task number to mark as COMPLETED: "))
                    if 0 <= task_number < len(Tasks):
                        Tasks[task_number]['status'] = 'COMPLETED'
                        print("Task marked as completed!")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Enter a valid number")

    elif option == 'VIEW':
         if not Tasks:
            print("No tasks found!!")
         else:
             for i in range(len(Tasks)):
                 t = Tasks[i]
                 print(f"Task {i} - {t['title']}, Status : {t['status']}")                
                    

    elif option =='EXIT':
        print ("Exited....")
        break
    


