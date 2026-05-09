# todo application

task_num  = input("Enter the number of tasks you want to add to your todo list: ")

todo_list = []
finished_tasks = []


for i in range(int(task_num)):

    task = input("Enter the task: ")
    todo_list.append(task)
    
    
print(todo_list)



f_task = input("Enter the task that is finished: ")

finished_tasks.append(f_task)

print("Finished tasks: ", finished_tasks)




