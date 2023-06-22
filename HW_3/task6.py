# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
#  Строки нумеруются начиная с единицы.
#  Слова выводятся отсортированными согласно кодировки Unicode.
#  Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

import  string

text = input('Введите текст: ')

my_list = text.split()

for i in range(len(my_list)):
    my_list[i] = my_list[i].strip(string.punctuation)

my_list.sort()

max_len = len(max(my_list, key=len))

for i, item in enumerate(my_list):
    print(f'{i + 1} {item : >{max_len}}' if i > 8 else f'{i + 1}  {item : >{max_len}}')