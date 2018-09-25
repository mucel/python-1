print("Welcome to the TODO task management program.")

todo_list = []

def add_new_task(tasks, task_status):
    task = ("Darāmais darb: ")
    task['status'] = ("task-status: ")
    tasks.appen

def remove_all_tasks(filename):
    os.remove(filename)
    return []

while True:
    task = input("Ludzu ievadiet daramo darbu: ")
    todo_list.append(task)
    new = input("Vai pievienot jaunu? (j/n) ")
    if new.lower() == "n" :
        break

fails = open('todo.txt', '+w')
print('Visi parveidotie darbi: ')
skaititajs = 1
for task in todo_list
    if todo_list[task]:
        statuss = 'IR'
    else:
        statuss = 'NAV'
    print('{} - {} Izdarits: {}'. format(skaititajs, task, statuss))
    fails.rite('{} - {} Izdarits: {}\n'. format(skaititajs, task, statuss))
    skaititajs = skaititajs + 1
fails.close()


print ("Beigas")
