

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