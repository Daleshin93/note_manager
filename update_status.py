status = input('Статус: ')
print(status)

statuses = {'1': 'В работе', '2': 'Отложено', '3': 'Выполнено'}  # Создал словарь для статусов
keys = list(statuses.keys())                                     # Создал список из ключей
values = list(statuses.values())                                 # Создал список из значений
list_key_values = [ f'{k}: {v}' for k, v in zip(keys, values) ]  # Объеденил списки с изменением формата
column_statuses ='\n'.join(list_key_values)                      # Форматирование для вывода в столбец
while True:                                                      # Создания цикла для изменнения статуса
    new_status = input(f'Выберите новый статус для заметки:\n'   # Присвоение переменной значения на основании ввода
          f'{column_statuses}\n')
    value = statuses.get(new_status)                             # Поиск значения из словаря по ключу
    if new_status in keys:                                       # Условие: если значение переменной есть в списке
        print(f'Статус заметки изменён на: {value}.')
        break
    elif new_status in values:                                   # Или же значение переменной есть в другом списке
        print(f'Статус заметки изменён на: {new_status}.')
        break
    else:
        print(f'Статус "{new_status}" не найден.')
