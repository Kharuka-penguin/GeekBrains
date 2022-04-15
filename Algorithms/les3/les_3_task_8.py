#8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
import numpy
import numpy as np

print("Построчно вводите значение матрицы 5х4")
matrix = [[int(input("Введите значение матрицы: ")) for i in range(4)] for j in range(4)]

summa = []
for line in matrix:
    sum_line = 0
    for i, item in enumerate(line):
        sum_line += item
        sum_in_list = [sum_line]
    summa.append(sum_in_list)

print(f'\nПолучится следующая матрица \n{np.concatenate((matrix, summa), axis=1)}')
