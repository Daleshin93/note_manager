username = input('Введите имя пользователя: ')
title = input('Заголовок заметки: ')
content = input('Описание заметки: ')
status = input('Статус: ')
created_date = input('Дата создания заметки, (укажите дату в формате "дд-мм-гггг"): ')
issue_date = input('Дата дедлайна: ')

temp_created_date = created_date[0:5]
temp_issue_date = issue_date[0:5]

print(f'Имя пользователя: {username}')
print(f'Заголовок: {title}')
print(f'Описание заметки: {content}')
print(f'Ваш статус: {status}')
print(f'Дата создания заметки: {temp_created_date}')
print(f'Дата дедлайна: {temp_issue_date}')