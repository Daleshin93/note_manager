from datetime import datetime

today = datetime.today()
format_today = datetime.strftime(today, '%d-%m-%Y')
dt_today = datetime.strptime(format_today, '%d-%m-%Y')

print(f'Текущая дата {format_today}')

while True:
    issue_date = input('Дата дедлайна, (укажите дату в формате "дд-мм-гггг"): ')
    try:
        dt_issue = datetime.strptime(issue_date, '%d-%m-%Y')
        break
    except ValueError:
        print('Неверный формат даты, введите в указаном формате.')

if dt_today < dt_issue:
    delta = dt_issue - dt_today
    if delta.days % 10 == 1:
        days = 'день'
    elif delta.days % 10 < 5:
        days = 'дня'
    else:
        days = 'дней'
    print(f'До дедлайна: {delta.days} {days}.')
elif dt_today > dt_issue:
    delta = dt_today - dt_issue
    if delta.days % 10 == 1 :
        days = 'день'
    elif delta.days % 10 < 5 :
        days = 'дня'
    else:
        days = 'дней'
    print(f'Внимание! Дедлайн истек {delta.days} {days} назад.')
elif dt_today == dt_issue:
    print(f'Дедлайн сегодня 😱.')
