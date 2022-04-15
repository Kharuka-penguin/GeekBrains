# Вывод: Алгоритм разобранный на уроке самый оптимальный с линейной зависимостью времени от дальности находимого числа

import timeit
import cProfile


# def eratosfen_sieve(serial_number, diapason_number=1000):
#     list_numbers = [i for i in range(diapason_number + 1)]
#     list_numbers[1] = 0
#     for i in range(2, diapason_number + 1):
#         if list_numbers[i] != 0:
#             j = i * 2
#             while j <= diapason_number:
#                 list_numbers[j] = 0
#                 j += i
#     sieve = [i for i in list_numbers if i != 0]
#     return sieve[serial_number - 1]

# print(eratosfen_sieve(159))

# $ python3 -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.eratosfen_sieve(10)"
# 1000 loops, best of 5: 203 usec per loop
# "les_4_task_2.eratosfen_sieve(50)"
# 1000 loops, best of 5: 203 usec per loop
# "les_4_task_2.eratosfen_sieve(100)"
# 1000 loops, best of 5: 205 usec per loop
# "les_4_task_2.eratosfen_sieve(165)"
# 1000 loops, best of 5: 203 usec per loop

# cProfile.run('eratosfen_sieve(165)')
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:5(eratosfen_sieve)    10
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:5(eratosfen_sieve)    50
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:5(eratosfen_sieve)    100
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:5(eratosfen_sieve)    165


# def eratosfen_set_subtraction(serial_number, diapason_number=1000):
#     sieve = set(range(2, diapason_number + 1))
#     count = 0
#     while sieve:
#         prime = min(sieve)
#         count += 1
#         sieve -= set(range(prime, diapason_number + 1, prime))
#         if count == serial_number:
#             return prime

# print(eratosfen_set_subtraction(159))

# $ python3 -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.eratosfen_set_subtraction(10)"
# 1000 loops, best of 5: 127 usec per loop
# "les_4_task_2.eratosfen_set_subtraction(50)"
# 1000 loops, best of 5: 285 usec per loop
# "les_4_task_2.eratosfen_set_subtraction(100)"
# 1000 loops, best of 5: 437 usec per loop
# "les_4_task_2.eratosfen_set_subtraction(165)"
# 1000 loops, best of 5: 601 usec per loop

# cProfile.run('eratosfen_set_subtraction(165)')
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:35(eratosfen_set_subtraction)     10
# 10    0.000    0.000    0.000    0.000 {built-in method builtins.min}
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:35(eratosfen_set_subtraction)     50
# 50    0.000    0.000    0.000    0.000 {built-in method builtins.min}
# 1    0.000    0.000    0.001    0.001 les_4_task_2.py:35(eratosfen_set_subtraction)     100
# 100    0.000    0.000    0.000    0.000 {built-in method builtins.min}
# 1    0.000    0.000    0.001    0.001 les_4_task_2.py:35(eratosfen_set_subtraction)     165
# 165    0.000    0.000    0.000    0.000 {built-in method builtins.min}

# def prime_number_search(serial_number, diapason_number=1000):
#     prime_number_count = 0
#     for number in range(2, diapason_number + 1):
#         divisor_count = 0
#         for divisor in range(2, number // 2 + 1):
#             if number % divisor == 0:
#                 divisor_count += 1
#         if divisor_count <= 0:
#             prime_number_count += 1
#         else:
#             continue
#         if prime_number_count == serial_number:
#             return number

# print(prime_number_search(159))

# $ python3 -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime_number_search(10)"
# 1000 loops, best of 5: 14.4 usec per loop
# "les_4_task_2.prime_number_search(50)"
# 1000 loops, best of 5: 554 usec per loop
# "les_4_task_2.prime_number_search(100)"
# 1000 loops, best of 5: 2.93 msec per loop
# "les_4_task_2.prime_number_search(165)"
# 1000 loops, best of 5: 9.7 msec per loop

# cProfile.run('prime_number_search(165)')
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:66(prime_number_search)   10
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:66(prime_number_search)   50
# 1    0.003    0.003    0.003    0.003 les_4_task_2.py:66(prime_number_search)   100
# 1    0.011    0.011    0.011    0.011 les_4_task_2.py:66(prime_number_search)   165