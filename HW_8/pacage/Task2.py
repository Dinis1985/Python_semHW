# Прочитайте созданный в прошлом задании csv файл без использования
# csv.DictReader. Распечатайте его как pickle строку.

__all__ = ['string']

import csv
import pickle


def string(csv_file):
    with open(csv_file, 'r', newline='') as f_c:
        csv_r = csv.reader(f_c, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
        data = []
        keys = []
        for i, item in enumerate(csv_r):
            dictionary = {}
            if i == 0:
                keys = item
            else:
                for j, elem in enumerate(item):
                    dictionary[keys[j]] = elem
            if len(dictionary) != 0:
                data.append(dictionary)
        res = pickle.dumps(data, protocol=pickle.DEFAULT_PROTOCOL)
        print(f'{res = }')


if __name__ == '__main__':
    string('file_tab.csv')