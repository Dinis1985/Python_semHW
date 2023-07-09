# Напишите функцию, которая преобразует pickle файл хранящий список словарей в
# табличный csv файл. Для тестированию возьмите pickle версию файла из предыдущей задачи.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

__all__ = ['transformation']

import pickle
import csv

def transformation(pickle_file, csv_file):
    with(open(pickle_file, 'rb') as f_p,
         open(csv_file, 'w', encoding='utf-8', newline='') as f_c):
        dictionary = pickle.load(f_p)
        new_csv = csv.DictWriter(f_c, fieldnames=['id', 'level', 'name'],
                                 dialect='excel-tab', quoting=csv.QUOTE_ALL)
        new_csv.writeheader()
        new_csv.writerows(dictionary)


if __name__ == '__main__':
    transformation('user.pickle', 'file_tab.csv')