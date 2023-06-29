# Напишите функцию, которая принимает на вход строку - абсолютный путь
# до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла,
# расширение файла.

def path_name_extension(path: str) -> tuple:
    path, name = path.rsplit('\\', 1)
    name, extension = name.split('.')
    return path, name, extension


path_to_file = r'C:\GB\Python_semHW\HW_5\Task1.py'
print(path_name_extension(path_to_file))