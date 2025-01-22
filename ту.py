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
column_titles ='\n'.join(format_titles)

content = input('Описание заметки: ')
status = input('Статус: ')
created_date = input('Дата создания заметки, (укажите дату в формате "дд-мм-гггг"): ')
issue_date = input('Дата дедлайна, (укажите дату в формате примера: "10 Января 2025"): ')

temp_created_date = created_date[0:-5]
temp_issue_date = issue_date[0:-5]

note = [username, titles, content, status, temp_created_date, temp_issue_date]

print(f'Имя пользователя: {note[0]} \n'
      f'Заголовки заметки: \n'
      f'{column_titles} \n'
      f'Описание заметки: {note[2]} \n'
      f'Статус заметки: {note[3]} \n'
      f'Дата создания заметки: {note[4]} \n'
      f'Дата дедлайна: {note[5]}')