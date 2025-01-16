username = input('Введите имя пользователя: ')
title1 = input('Введите первый заголовок заметки: ')
title2 = input('Второй заголовок заметки: ')
title3 = input('Третий заголовок заметки: ')
content = input('Описание заметки: ')
status = input('Статус: ')
created_date = input('Дата создания заметки, (укажите дату в формате "дд-мм-гггг"): ')
issue_date = input('Дата дедлайна: ')

title = [title1, title2, title3]

temp_created_date = created_date[0:5]
temp_issue_date = issue_date[0:5]

print(f'Имя пользователя: {username}')
print(f'Заголовки заметки:\n 1: {title[0]} \n 2: {title[1]} \n 3: {title[2]}')
print(f'Описание заметки: {content}')
print(f'Ваш статус: {status}')
print(f'Дата создания заметки: {temp_created_date}')
print(f'Дата дедлайна: {temp_issue_date}')