# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

a_list = [random.randint(0, 100) for i in range(1, 30)]
print(f'\nПолучился следующий массив {a_list}')

max = 0
ind_max = 0
min = 100
ind_min = 0

for i in enumerate(a_list):
    if i[1] < min:
        min = i[1]
        ind_min = i[0]
    if i[1] > max:
        max = i[1]
        ind_max = i[0]

minimum = ind_min
maximum = ind_max
#print(min, ind_min)
#print(max, ind_max)

sum_vlevo = -a_list[ind_min]
sum_vpravo = -a_list[ind_max]

for i in enumerate(a_list):
    if ind_min < ind_max:
        sum_vlevo += a_list[ind_min]
        ind_min += 1
    if ind_max < ind_min:
        sum_vpravo += a_list[ind_max]
        ind_max += 1

if minimum > maximum:
    print(f'Сумма элементов, находящихся между минимальным {min} и максимальным {max} элементами равно {sum_vpravo}')
if maximum > minimum:
    print(f'Сумма элементов, находящихся между минимальным {min} и максимальным {max} элементами равно {sum_vlevo}')

