# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов.
# * При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>

__all__ = ['rename_files']

import os

def rename_files(new_name: str, ext: str, new_ext: str):
    path = r'C:\GB\Python_semHW\HW_7\New'
    files = os.listdir(path)
    for position, item in enumerate(files, 1):
        file_ext = item.split('.')[1]
        if file_ext == ext:
            file_name = os.path.join(path, f'{item.split(".")[0]}_{new_name}_{position}.{new_ext}')
            original_name = os.path.join(path, item)
            os.rename(original_name, file_name)


if __name__ == '__main__':
    rename_files('new', 'txt', 'jpg')
