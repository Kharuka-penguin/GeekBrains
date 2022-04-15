#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = [[random.randint(0, 100) for i in range(4)] for j in range(4)]
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()

print('-' * (len(matrix)) * 5)
min_list = []

for i in range(4):
    min_column = 100
    for line in matrix:
        if line[i] < min_column:
            min_column = line[i]
    min_list.append(min_column)
print(f'максимальный элемент среди минимальных элементов столбцов матрицы = {max(min_list)}')
