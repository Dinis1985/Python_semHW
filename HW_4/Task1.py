# Напишите функцию для транспонирования матрицы

import numpy as np


def transposition(matrix):
    transpose_matrix = matrix.transpose()
    return transpose_matrix


matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix, transposition(matrix), sep='\n')