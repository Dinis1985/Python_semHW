# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 100
ATTEMPTS = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range (ATTEMPTS):
    user_num = int(input('Угадай число, которое я загадала '))
    if user_num == num:
        print('Молодец! Угадал!')
        break
    elif user_num > num:
        print('Неверно, бери меньше')
    elif user_num < num:
        print('Неверно, бери больше')
else:
    print('Попытки закончились! Ты проиграл!')