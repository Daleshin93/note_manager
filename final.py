username = input('Введите имя пользователя: ')
titles = [input('Введите первый заголовок заметки: '),
         input('Второй заголовок заметки: '),
         input('Третий заголовок заметки: ')]
content = input('Описание заметки: ')
status = input('Статус: ')
created_date = input('Дата создания заметки, (укажите дату в формате "дд-мм-гггг"): ')
issue_date = input('Дата дедлайна, (укажите дату в формате примера: "10 Января 2025"): ')

temp_created_date = created_date[0:-5]
temp_issue_date = issue_date[0:-5]

note = [username, titles, content, status, temp_created_date, temp_issue_date]

print(f'Имя пользователя: {note[0]} \n'
      f'Заголовки заметки:\n '
      f'1: "{note[1][0]}" \n '
      f'2: "{note[1][1]}" \n '
      f'3: "{note[1][2]}" \n '
      f'Описание заметки: {note[2]} \n'
      f'Ваш статус: {note[3]} \n'
      f'Дата создания заметки: {note[4]} \n'
      f'Дата дедлайна: {note[5]}')