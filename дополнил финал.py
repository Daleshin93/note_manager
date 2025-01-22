username = input('Введите имя пользователя: ')
titles = []
user_input = input('Введите заголовок заметки: ')
titles.append(user_input)
while True:
    user_input = input('Введите дополнительные заголовки '
                       '(или оставьте пустым для завершения): ')
    if user_input == '':
        break
    titles.append(user_input)

unic_titles = list(dict.fromkeys(titles))
format_titles = [f'- {t}' for t in unic_titles]
titles ='\n'.join(format_titles)

content = input('Описание заметки: ')
status = input('Статус: ')
created_date = input('Дата создания заметки, (укажите дату в формате "дд-мм-гггг"): ')
issue_date = input('Дата дедлайна, (укажите дату в формате примера: "10 Января 2025"): ')

temp_created_date = created_date[0:-5]
temp_issue_date = issue_date[0:-5]

note = [username, titles, content, status, temp_created_date, temp_issue_date]

print(f'\nИмя пользователя: {note[0]} \n'
      f'Заголовки заметки: \n'
      f'{note[1]} \n'
      f'Описание заметки: {note[2]} \n'
      f'Статус заметки: {note[3]} \n'
      f'Дата создания заметки: {note[4]} \n'
      f'Дата дедлайна: {note[5]}\n')

statuses = ['В работе', 'Отложено', 'Выполнено']

while True:
    new_status = input(f'Выберите новый статус для заметки:\n'
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