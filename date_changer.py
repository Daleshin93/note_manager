username = 'Дмитрий'
title = 'Заголовок'
content = 'Описание'
status = 'В работе'
created_date = '13-01-2025'
issue_date = '14-01-2025'

temp_created_date = created_date[0:5]
temp_issue_date = issue_date[0:5]

print(f'Имя пользователя: {username}')
print(f'Заголовок: {title}')
print(f'Описание заметки: {content}')
print(f'Ваш статус: {status}')
print(f'Дата создания заметки: {temp_created_date}')
print(f'Дата дедлайна: {temp_issue_date}')

