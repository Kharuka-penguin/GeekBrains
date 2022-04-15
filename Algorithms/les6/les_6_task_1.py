# les_1_task_6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.

# В этом задании решение сделано через модуль sys, разобранном на лекции.
# Вывод: решение через кортеж представляется самым лучшим с точки зрения выделения памяти, далее список и потом словарь.

import sys
print(sys.version, sys.platform)


# --------------------------- через list --------------------------------
def tri_list(list_val):
    list_val.sort()
    print(f'\nВариант через список:')
    show_size(list_val)
    if list_val[2] < (list_val[0] + list_val[1]):
        if list_val[0] == list_val[1] == list_val[2]:
            return f'Треугольник из таких отрезков будет РАВНОСТОРОННИМ.'
        elif list_val[0] == list_val[1] or list_val[1] == list_val[2] or list_val[2] == list_val[0]:
            return f'Треугольник из таких отрезков будет РАВНОБЕДРЕННЫМ.'
        else:
            return f'Треугольник из таких отрезков будет РАЗНОСТОРОННИМ.'
    else:
        return f'Треугольник из таких отрезков не получится.'


# --------------------------- через tuple --------------------------------
def tri_tuple(tuple_val):
    sorted_tuple_val = tuple(sorted(tuple_val))
    print(f'\nВариант через кортеж:')
    show_size(tuple_val)
    if sorted_tuple_val[2] < (sorted_tuple_val[0] + sorted_tuple_val[1]):
        if sorted_tuple_val[0] == sorted_tuple_val[1] == sorted_tuple_val[2]:
            return f'Треугольник из таких отрезков будет РАВНОСТОРОННИМ.'
        elif sorted_tuple_val[0] == sorted_tuple_val[1] or sorted_tuple_val[1] == sorted_tuple_val[2] \
                or sorted_tuple_val[2] == sorted_tuple_val[0]:
            return f'Треугольник из таких отрезков будет РАВНОБЕДРЕННЫМ.'
        else:
            return f'Треугольник из таких отрезков будет РАЗНОСТОРОННИМ.'
    else:
        return f'Треугольник из таких отрезков не получится.'


# --------------------------- через dict ---------------------------------
def tri_dict(dict_val):
    sorted_dict_val = sorted(dict_val.values())
    print(f'\nВариант через словарь:')
    show_size(dict_val)
    if sorted_dict_val[2] < (sorted_dict_val[0] + sorted_dict_val[1]):
        if dict_val.get(1) == dict_val.get(2) == dict_val.get(3):
            return f'Треугольник из таких отрезков будет РАВНОСТОРОННИМ.'
        elif dict_val.get(1) == dict_val.get(2) or dict_val.get(1) == dict_val.get(3) \
                or dict_val.get(2) == dict_val.get(3):
            return f'Треугольник из таких отрезков будет РАВНОБЕДРЕННЫМ.'
        else:
            return f'Треугольник из таких отрезков будет РАЗНОСТОРОННИМ.'
    else:
        return f'Треугольник из таких отрезков не получится.'


def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


if __name__ == '__main__':
    a, b, c = map(int, input('Введите через пробел длины отрезков треугольника: ').split(' '))
    print(tri_list([a, b, c]))
    print(tri_tuple((a, b, c)))
    print(tri_dict({1: a, 2: b, 3: c}))


# 3.9.7 (default, Sep 10 2021, 14:59:43)
# [GCC 11.2.0] linux
# Введите через пробел длины отрезков треугольника: 5 6 7
#
# Вариант через список:
#  type= <class 'list'>, size= 80, object= [5, 6, 7]
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 6
# 	 type= <class 'int'>, size= 28, object= 7
# Треугольник из таких отрезков будет РАЗНОСТОРОННИМ.
#
# Вариант через кортеж:
#  type= <class 'tuple'>, size= 64, object= (5, 6, 7)
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 6
# 	 type= <class 'int'>, size= 28, object= 7
# Треугольник из таких отрезков будет РАЗНОСТОРОННИМ.
#
# Вариант через словарь:
#  type= <class 'dict'>, size= 232, object= {1: 5, 2: 6, 3: 7}
# 	 type= <class 'tuple'>, size= 56, object= (1, 5)
# 		 type= <class 'int'>, size= 28, object= 1
# 		 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'tuple'>, size= 56, object= (2, 6)
# 		 type= <class 'int'>, size= 28, object= 2
# 		 type= <class 'int'>, size= 28, object= 6
# 	 type= <class 'tuple'>, size= 56, object= (3, 7)
# 		 type= <class 'int'>, size= 28, object= 3
# 		 type= <class 'int'>, size= 28, object= 7
# Треугольник из таких отрезков будет РАЗНОСТОРОННИМ.


