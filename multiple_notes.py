from datetime import datetime

print('\nДобро пожаловать в "Менеджер заметок". Вы можете добавить заметку.\n')
statuses = ['Новая', 'В работе', 'Выполнено']
notes = []

while True:
    while True:
        username = input('Введите имя пользователя: ')
        if username != '':
            break
        else:
            print('Поле не может быть пустым')

    while True:
        titles = input('Введите заголовок заметки: ')
        if titles != '':
            break
        else:
            print('Поле не может быть пустым')


    content = input('Описание заметки: ')


    while True:
        status = input(f'\nВыберите статус для заметки:\n'
                           f'1- {statuses[0]}\n'
                           f'2- {statuses[1]}\n'
                           f'3- {statuses[2]}\n')
        if status in statuses:
            status = status
            print(f'\nСтатус заметки: {status}.\n')
            break
        elif status.isdigit():
            number = int(status)
            if 1 <= number <= 3:
                status = statuses[number - 1]
                print(f'Статус заметки: {statuses[number - 1]}.\n')
                break
            else:
                print(f'\nСтатус "{status}" не найден, повторите попытку.')
        else:
            print(f'\nСтатус "{status}" не найден, повторите попытку.')


    while True:
        created_date = input('Дата создания заметки, (укажите дату в формате "дд-мм-гггг"):\n')
        try:
            dt_created = datetime.strptime(created_date, '%d-%m-%Y')
            break
        except ValueError:
            print('Неверный формат даты, введите в указаном формате.')


    while True:
        issue_date = input('Дата дедлайна, (укажите дату в формате "дд-мм-гггг"):\n')
        try:
            dt_issue = datetime.strptime(issue_date, '%d-%m-%Y')
            break
        except ValueError:
            print('Неверный формат даты, введите в указаном формате.')


    note = {'Имя пользователя': username,
             'Заголовок': titles,
             'Описание заметки': content,
             'Ваш статус': status,
             'Дата создания заметки': created_date,
             'Дата дедлайна': issue_date}
    notes.append(note)


    while True:
        user_input = input('Хотите добавить заметку? (да\нет):\n')
        if user_input == 'да' or user_input == 'нет':
            break
        else:
            print('Попробуйте снова: ')
    if user_input == 'нет':
        break

print(f'\nСписок заметок: ')
for i, note in enumerate(notes, start=1):
    print(f'\nЗаметка {i}: 📝')
    for k, v in note.items():
        print(f'{k}: {v}')