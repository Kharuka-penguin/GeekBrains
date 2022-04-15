# Задача из 2 урока №4: Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество
# элементов (n) вводится с клавиатуры.

########### Вывод: оптимальный вариант - через цикл!!! Он лучше по скорости и по количеству вложенных вызовов

import timeit
import cProfile
# num = int(input("Введите число n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…: "))


# def sum_elem(qty, elem=1, summa_el=0):
#     if qty == 0:
#         return summa_el
#     if qty >= 1:
#         summa_el += elem
#         elem /= -2
#         return sum_elem(qty-1, elem, summa_el)


#$ python3 -m timeit -n 1000 -s "import les4_task_1" "les4_task_1.sum_elem(10)"
# 1000 loops, best of 5: 1.79 usec per loop
# "les4_task_1.sum_elem(100)"
# 1000 loops, best of 5: 18.1 usec per loop
# "les4_task_1.sum_elem(300)"
# 1000 loops, best of 5: 60.3 usec per loop
# "les4_task_1.sum_elem(500)"
# 1000 loops, best of 5: 103 usec per loop

# cProfile.run('sum_elem(500)')
# 11/1    0.000    0.000    0.000    0.000 les_4_task_1.py:8(sum_elem)     10
# 101/1    0.000    0.000    0.000    0.000 les_4_task_1.py:8(sum_elem)    100
# 301/1    0.000    0.000    0.000    0.000 les_4_task_1.py:8(sum_elem)    300
# 501/1    0.000    0.000    0.000    0.000 les_4_task_1.py:8(sum_elem)    500


# def sum_loop(while_to):
#     count = 1
#     number = 1
#     sum_number = 1
#     while count < while_to:
#         number /= -2
#         sum_number = sum_number + number
#         count += 1
#     return sum_number


#$ python3 -m timeit -n 1000 -s "import les4_task_1" "les4_task_1.sum_loop(10)"
# 1000 loops, best of 5: 825 nsec per loop
# "les4_task_1.sum_loop(100)"
# 1000 loops, best of 5: 7.9 usec per loop
# "les4_task_1.sum_loop(300)"
# 1000 loops, best of 5: 24 usec per loop
# "les4_task_1.sum_loop(500)"
# 1000 loops, best of 5: 41.6 usec per loop

# cProfile.run('sum_loop(500)')
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:33(sum_loop)   10
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:33(sum_loop)   100
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:33(sum_loop)   300
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:33(sum_loop)   500


# def sum_gen(numb):
#     def generator(number, element: float = 1):
#         if number > 0:
#             yield element
#             yield from generator(number-1, element / -2)
#     sum_list = sum(list(generator(numb)))
#     return sum_list

# $ python3 -m timeit -n 1000 -s "import les4_task_1" "les4_task_1.sum_gen(10)"
# 1000 loops, best of 5: 3.67 usec per loop
# "les4_task_1.sum_gen(100)"
# 1000 loops, best of 5: 159 usec per loop
# "les4_task_1.sum_gen(300)"
# 1000 loops, best of 5: 1.64 msec per loop
# "les4_task_1.sum_gen(500)"
# 1000 loops, best of 5: 5.18 msec per loop

# cProfile.run('sum_gen(500)')
# 66/11    0.000    0.000    0.000    0.000 les_4_task_1.py:61(generator)        10
# 5151/101    0.001    0.000    0.001    0.000 les_4_task_1.py:61(generator)     100
# 45451/301    0.006    0.000    0.006    0.000 les_4_task_1.py:61(generator)    300
# 125751/501    0.017    0.000    0.017    0.000 les_4_task_1.py:61(generator)   500

# if __name__ == '__main__':
#     if num < 0:
#         print('Введите целое натуральное число')
#     elif num == 0:
#         print('0')
#     elif num == 1:
#         print('1')
#     else:
#         print(f'Вариант через классическую рекурсию: {sum_elem(num)}')
#         print(f'Вариант через цикл: {sum_loop(num)}')
#         print(f'Вариант через генератор: {sum_gen(num)}')
