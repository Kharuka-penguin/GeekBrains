# les_3_task_7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между
# собой (оба минимальны), так и различаться.

# В данной задании для измерения памяти применяется модуль guppy к различным алгоритмам сортировки массива
# (пузырьком, шейкерный и пирамидальный). Вывод: лучший - шейкерный, далее пирамидальный, последний пузырьком.

import random
from guppy import hpy

heap = hpy()
A_list = [random.randint(1, 2000) for i in range(1, 1000)]

# ------------------ Сортировка пузырьком ------------------------------------
heap.setref()

a_list = A_list.copy()
ii = 0
while ii < len(a_list) - 1:
    j = 0
    while j < len(a_list) - 1 - ii:
        if a_list[j] > a_list[j+1]:
            a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
        j += 1
    ii += 1

heap_status_1 = heap.heap()
print('Размер памяти необходимый под сортировку пузырьком:', heap_status_1.size, 'байт')
print(f'Минимальные элементы через сортировку пузырьком: {a_list[0]} и {a_list[1]}')

# ------------------ Шейкерная сортировка ----------------------------------
heap.setref()

a_list = A_list.copy()
left = 0
right = len(a_list) - 1
while left <= right:
    for i in range(left, right, +1):
        if a_list[i] > a_list[i + 1]:
            a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
    right -= 1
    for i in range(right, left, -1):
        if a_list[i - 1] > a_list[i]:
            a_list[i], a_list[i - 1] = a_list[i - 1], a_list[i]
    left += 1

heap_status_2 = heap.heap()
print('Размер памяти необходимый под шейкерую сортировку:', heap_status_2.size, 'байт')
print(f'Минимальные элементы через шейкерную сортировку: {a_list[0]} и {a_list[1]}')

# -------------------- Пирамидальная сортировка --------------------------------
heap.setref()

a_list = A_list.copy()


def sift_down(parent, limit):
    item = a_list[parent]
    while True:
        child = (parent << 1) + 1
        if child >= limit:
            break
        if child + 1 < limit and a_list[child] < a_list[child + 1]:
            child += 1
        if item < a_list[child]:
            a_list[parent] = a_list[child]
            parent = child
        else:
            break
    a_list[parent] = item


length = len(a_list)
for index in range((length >> 1) - 1, -1, -1):
    sift_down(index, length)
for index in range(length - 1, 0, -1):
    a_list[0], a_list[index] = a_list[index], a_list[0]
    sift_down(0, index)

heap_status_3 = heap.heap()
print('Размер памяти необходимый под пирамидальную сортировку:', heap_status_3.size, 'байт')
print(f'Минимальные элементы через пирамидальную сортировку: {a_list[0]} и {a_list[1]}')


# Размер памяти необходимый под сортировку пузырьком: 8692 байт
# Минимальные элементы через сортировку пузырьком: 2 и 2
# Размер памяти необходимый под шейкерую сортировку: 8540 байт
# Минимальные элементы через шейкерную сортировку: 2 и 2
# Размер памяти необходимый под пирамидальную сортировку: 8620 байт
# Минимальные элементы через пирамидальную сортировку: 2 и 2










