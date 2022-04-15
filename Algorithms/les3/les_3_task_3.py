# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a = []
n = int(input('Введи колличество чисел в массиве: '))

for m in range(1, n+1):
    a.append(random.randint(1, 1000))
print(f'Получился такой массив {a}')

maximum = a[0]
minimum = a[0]
ind_max = 0
ind_min = 0

for item in enumerate(a):
    if item[1] > maximum:
        maximum = item[1]
        ind_max = item[0]
    if item[1] < minimum:
        minimum = item[1]
        ind_min = item[0]
print(f'Максимальное значение в массиве {maximum}, индекс максимального значения в массиве {ind_max}')
print(f'Минимальное значение в массиве {minimum}, индекс минимального значения в массиве {ind_min}')
a[ind_min], a[ind_max] = a[ind_max], a[ind_min]
print(f'После изменения местами максимально и минимального значений получился следующий массив {a}')