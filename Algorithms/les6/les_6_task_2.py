# les_2_task_4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество
# # элементов (n) вводится с клавиатуры.

# В этом задании решение сделано через модуль memory_profiler. Рассмотрено профилирование 3‑х разных алгоритмов решения
# задачи. Вывод: лучше всего - решение через цикл: занимает памяти меньше всех на протяжении исполнения всей
# программы; решение через генератор в процессе исполнения занимает чуть больше памяти; решение через рекурсию
# занимает значительно больше места и к тому же за счет постоянного перевхождения в функцию профилируется очень долго
# (каждое вхождение профилируется отдельно).

from memory_profiler import profile
import sys

print(sys.version, sys.platform)
# num = int(input("Введите число n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…: "))
num = 150


# @profile
# def sum_elem(qty, elem=1, summa_el=0):                # Классическая рекурсия
#     if qty == 0:
#         return summa_el
#     if qty >= 1:
#         summa_el += elem
#         elem /= -2
#         return sum_elem(qty - 1, elem, summa_el)

# @profile
# def sum_loop(while_to):                                # Через цикл
#     count = 1
#     number = 1
#     sum_number = 1
#     while count < while_to:
#         number /= -2
#         sum_number = sum_number + number
#         count += 1
#     return sum_number


@profile
def sum_gen(numb):                                      # Через генератор
    def generator(number, element: float = 1):
        if number > 0:
            yield element
            yield from generator(number - 1, element / -2)
    sum_list = sum(list(generator(numb)))
    return sum_list


if __name__ == '__main__':
    if num < 0:
        print('Введите целое натуральное число')
    elif num == 0:
        print('0')
    elif num == 1:
        print('1')
    else:
        # print(f'Вариант через классическую рекурсию: {sum_elem(num)}')
        # print(f'Вариант через цикл: {sum_loop(num)}')
        print(f'Вариант через генератор: {sum_gen(num)}')


# 3.9.7 (default, Sep 10 2021, 14:59:43)
# [GCC 11.2.0] linux

# -------------------- Результаты профилирования ----------------------

# ------ Классическая рекурсия:

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     12     18.5 MiB     18.0 MiB         151   @profile
#     13                                         def sum_elem(qty, elem=1, summa_el=0):
#     14     18.5 MiB      0.0 MiB         151       if qty == 0:
#     15     18.5 MiB      0.0 MiB           1           return summa_el
#     16     18.5 MiB      0.3 MiB         150       if qty >= 1:
#     17     18.5 MiB      0.0 MiB         150           summa_el += elem
#     18     18.5 MiB      0.3 MiB         150           elem /= -2
#     19     18.5 MiB      0.0 MiB         150           return sum_elem(qty - 1, elem, summa_el)
#
#
# Вариант через классическую рекурсию: 0.6666666666666667


# ------ Через цикл:

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     23     17.2 MiB     17.2 MiB           1   @profile
#     24                                         def sum_loop(while_to):                       # Через цикл
#     25     17.2 MiB      0.0 MiB           1       count = 1
#     26     17.2 MiB      0.0 MiB           1       number = 1
#     27     17.2 MiB      0.0 MiB           1       sum_number = 1
#     28     17.2 MiB      0.0 MiB         150       while count < while_to:
#     29     17.2 MiB      0.0 MiB         149           number /= -2
#     30     17.2 MiB      0.0 MiB         149           sum_number = sum_number + number
#     31     17.2 MiB      0.0 MiB         149           count += 1
#     32     17.2 MiB      0.0 MiB           1       return sum_number
#
#
# Вариант через цикл: 0.6666666666666667


# ------ Через генератор:

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     35     17.1 MiB     17.1 MiB           1   @profile
#     36                                         def sum_gen(numb):                            # Через генератор
#     37     17.4 MiB      0.3 MiB         152       def generator(number, element: float = 1):
#     38     17.4 MiB      0.0 MiB         151           if number > 0:
#     39     17.4 MiB      0.0 MiB         300               yield element
#     40     17.4 MiB      0.0 MiB       11325               yield from generator(number - 1, element / -2)
#     41     17.4 MiB      0.0 MiB           1       sum_list = sum(list(generator(numb)))
#     42     17.4 MiB      0.0 MiB           1       return sum_list
#
#
# Вариант через генератор: 0.6666666666666667

