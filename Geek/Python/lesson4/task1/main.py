"""
Напишите функцию для транспонирования матрицы
"""


def transpose_matrix(matrix):
    # Получаем количество строк и столбцов исходной матрицы
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Создаем новую матрицу с транспонированными размерами
    transposed = [[0] * rows for _ in range(cols)]

    # Заполняем новую матрицу значениями из исходной матрицы
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose_matrix(matrix)

# Выводим транспонированную матрицу
for row in transposed_matrix:
    print(row)