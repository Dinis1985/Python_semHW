# ✔Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры: ✔расширение
# ✔минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔количество файлов, по умолчанию 42 ✔Имя файла и его размер должны быть в рамках
# переданного диапазона.

# ✔Доработаем предыдущую задачу. ✔Создайте новую функцию которая генерирует файлы с
# разными расширениями. ✔Расширения и количество файлов функция принимает в качестве
# параметров. ✔Количество переданных расширений может быть любым.
# ✔Количество файлов для каждого расширения различно.
# ✔Внутри используйте вызов функции из прошлой задачи.

# Дорабатываем функции из предыдущих задач.
# * Генерируйте файлы в указанную директорию — отдельный параметр функции.
# * Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# * Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

__all__ = ['create_files']

import os
import random
import string


def create(extension, dir_name: str, min_length=6, max_length=30, min_size=256, max_size=4096, num_files=4):
    for _ in range(num_files):
        name_length = random.randint(min_length, max_length)
        file_name = ''.join(random.choices(
            string.ascii_letters + string.digits, k=name_length)) + '.' + extension
        file_size = random.randint(min_size, max_size)
        random_bytes = ''.join(random.choices(
            string.ascii_letters + string.digits, k=file_size)).encode('utf-8')
        file_path = os.path.join(dir_name, file_name)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        if not os.path.exists(file_path):
            with open(file_path, 'wb') as f:
                f.write(random_bytes)


def create_files(**kwargs):
    for ext, num in kwargs.items():
        create(
            ext, r'C:\GB\Python_semHW\HW_7\New', num_files=num)


if __name__ == '__main__':
    create_files(zip=3, jpg=2, txt=4)