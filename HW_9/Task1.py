
# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.



import csv
import datetime
import json
import math
import os.path
from random import randint as rnd


LINES = 100
ARGS = 3
MIN_LIMIT = -100
MAX_LIMIT = 100


def deco_csv(function):
    create_csvfile()

    def wrapper():
        with open('coefficiens.csv', 'r', encoding='UTF-8') as file:
            data = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            for coef in data:
                if coef and coef[0] != 0:
                    function(*coef)

    return wrapper


def json_save(func):
    result = {}
    if os.path.exists('decision.json'):
        with open('decision.json', 'r', encoding='UTF-8') as file:
            result = json.load(file)
    else:
        with open('decision.json', 'w', encoding='UTF-8') as file:
            json.dump(result, file)
    def wrapper(*args):
        roots = func(*args)
        solve_dict = {'a': args[0], 'b': args[1], 'c': args[2], 'roots': roots}
        res_key = f'{datetime.datetime.now()}'[:-7]
        result[res_key] = result.get(res_key) + [solve_dict] if result.get(res_key) else [solve_dict]
        with open('decision.json', 'w', encoding='UTF-8', ) as file:
            json.dump(result, file, indent=4, ensure_ascii=False)
        return roots
    return wrapper


def create_csvfile():
    my_list = []
    for _ in range(ARGS):
        my_list.append(rnd(MIN_LIMIT, MAX_LIMIT + 1))
    for i in range(LINES):
        for j in range(ARGS):
            my_list[j] = rnd(MIN_LIMIT, MAX_LIMIT + 1)
            if my_list[j] == 0:
                my_list[j] = 1
        with open('coefficiens.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(my_list)


@deco_csv
@json_save
def equation(*args):
    a, b, c = args
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return round(x1, 2), round(x2, 2)
    elif d == 0:
        x = -b / (2 * a)
        return round(x, 2)


equation()