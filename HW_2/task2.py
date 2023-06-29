# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление. Функцию hex используйте
# для проверки своего результата.

DIGIT_16 = '0123456789abcdef'
BASE = 16

hexadecimal = {key: value for key, value in enumerate(DIGIT_16)}


def my_func(base: int, number: int):
    base_num = []
    while number > 0:
        base_num.append(hexadecimal[number % base])
        number //= base
    base_num.reverse()
    for i in range(len(base_num)):
        print(base_num[i], end='')
    print()

num = int(input('Введите число: '))

my_func(BASE, num)
print(hex(num))