status = input('Статус: ')
print(f'Текуший статус: {status}')
statuses = ['В работе', 'Отложено', 'Выполнено']

while True:
    new_status = input(f'\nВыберите новый статус для заметки:\n'
                       f'1- {statuses[0]}\n'
                       f'2- {statuses[1]}\n'
                       f'3- {statuses[2]}\n')
    if new_status in statuses:
        status = new_status
        print(f'\nСтатус заметки изменён на: {new_status}.')
        break
    elif new_status.isdigit():
        number = int(new_status)
        if 1 <= number <= 3:
            status = statuses[number - 1]
            print(f'\nСтатус заметки изменён на: {statuses[number - 1]}.')
            break
        else:
            print(f'\nСтатус "{new_status}" не найден, повторите попытку.')
    else:
        print(f'\nСтатус "{new_status}" не найден, повторите попытку.')


print(f'\nСтатус заметки: {status}')
