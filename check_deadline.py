from datetime import datetime

while True:
    current_date = input('Дата создания заметки, (укажите дату в формате "дд-мм-гггг"): ')
    try:
        dt_current = datetime.strptime(current_date, '%d-%m-%Y')
        break
    except ValueError:
        print('Неверный формат даты, введите в указаном формате.')

print(f'Текущая дата {current_date}')

while True:
    issue_date = input('Дата дедлайна, (укажите дату в формате "дд-мм-гггг"): ')
    try:
        dt_issue = datetime.strptime(issue_date, '%d-%m-%Y')
        break
    except ValueError:
        print('Неверный формат даты, введите в указаном формате.')

if dt_current < dt_issue:
    delta = dt_issue - dt_current
    if delta.days % 10 == 1:
        days = 'день'
    elif delta.days % 10 < 5:
        days = 'дня'
    else:
        days = 'дней'
    print(f'До дедлайна: {delta.days} {days}.')
elif dt_current > dt_issue:
    delta = dt_current - dt_issue
    if delta.days % 10 == 1 :
        days = 'день'
    elif delta.days % 10 < 5 :
        days = 'дня'
    else:
        days = 'дней'
    print(f'Внимание! Дедлайн истек {delta.days} {days} назад.')
elif dt_current == dt_issue:
    print(f'Дедлайн сегодня 😱.')

