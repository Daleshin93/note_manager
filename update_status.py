
status = input('Статус: ')
print(status)

statuses = {'1': 'В работе', '2': 'Отложено', '3': 'Выполнено'}  # Создал словарь для статусов
keys = list(statuses.keys())                                     # Создал список из ключей
values = list(statuses.values())                                 # Создал список из значений
list_key_values = [ f'{k}: {v}' for k, v in zip(keys, values) ]  # Объеденил списки с изменением формата
column_statuses ='\n'.join(list_key_values)                      # Для вывода в столбец
while True:                                                      # Создания цикла для изменнения статуса
    new_status = input(f'Выберите новый статус для заметки:\n'   #
          f'{column_statuses}\n')
    key = new_status                                             # Присвоение переменной значения на основании ввода
    value = statuses.get(key)                                    # Поиск значения из словаря по ключу (== None если ключа нет в словаре)
    if value is not None:                                        # Условие: если значение не является "None"
        print(f'Статус заметки изменён на: {value}.')
        break
    else:
        print(f'{key} не найден.')

