status = input('Статус: ')
note = ['username', 'titles', 'content', status, 'temp_created_date', 'temp_issue_date']
statuses = ['В работе', 'Отложено', 'Выполнено']

while True:
    new_status = input(f'\nВыберите новый статус для заметки:\n'
                       f'1- {statuses[0]}\n'
                       f'2- {statuses[1]}\n'
                       f'3- {statuses[2]}\n')
    if new_status in statuses:
        note[3] = new_status
        print(f'\nСтатус заметки изменён на: {new_status}.')
        break
    elif new_status == '1':
        note[3] = statuses[0]
        print(f'\nСтатус заметки изменён на: {statuses[0]}.')
        break
    elif new_status == '2':
        note[3] = statuses[1]
        print(f'\nСтатус заметки изменён на: {statuses[1]}.')
        break
    elif new_status == '3':
        note[3] = statuses[2]
        print(f'\nСтатус заметки изменён на: {statuses[2]}.')
        break
    else:
        print(f'\nСтатус "{new_status}" не найден, повторите попытку.')

print(f'\nИмя пользователя: {note[0]} \n'
      f'Заголовки заметки: \n'
      f'{note[1]} \n'
      f'Описание заметки: {note[2]} \n'
      f'Статус заметки: {note[3]} \n'
      f'Дата создания заметки: {note[4]} \n'
      f'Дата дедлайна: {note[5]}')