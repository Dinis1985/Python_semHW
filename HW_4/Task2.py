# Напишите функцию принимающую на вход только ключевые параметры и
# возвращающую словарь, где ключ — значение переданного аргумента, а значение —
# имя аргумента. Если ключ не хешируем, используйте его строковое представление

import typing

def func(**kwargs):
    my_dict = {}
    for name, value in kwargs.items():
        if not isinstance(value, typing.Hashable):
            my_dict[str(value)] = name
        else:
            my_dict[value] = name
    return my_dict

print(func(x=7, y=[1, 2, 3]))