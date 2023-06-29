#  Пользователь вводит строку текста.
#  Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
#  Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
#  Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

import re

text = input('Введите текст: ')
text = re.sub('\W+', '', text)

my_dict = {key: text.count(key) for (value, key) in enumerate(text)}

new_dict = {}

for char in text:
    new_dict[char] = new_dict.get(char, 0) + 1

print(my_dict)
print(new_dict)

# совпадают, т.к. добавляются в одинаковом порядке


