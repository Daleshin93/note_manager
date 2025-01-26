titles = []                                           # Создание списка

while True:                                           # Создание цикла
    user_input = input('Введите заголовок '
                       '(или оставьте пустым для завершения): ')
    if user_input in titles:
        print(f'Заголовок {user_input} уже существует')
    elif user_input == '':
        break                                         # выполняется функция остановки цикла.
    else:
        titles.append(user_input)                     # Добавляем значение в список.


format_titles = [f'- {t}' for t in titles]            # Форматирование списка, добавляем "-" к каждому элементу

column_titles ='\n'.join(format_titles)               # Объеденение списка, методом .join(), в одну строку, с
                                                      # использованием символа новой строки после каждого элемента
                                                      # списка, позволило вывести список в столбец.
print(f'Заголовки заметки: \n'
      f'{column_titles}')