# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import randint

my_list = [randint(0, 49) for i in range(10)]
print(my_list)


def merge_two_list(list1, list2):
    merge_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merge_list.append(list1[i])
            i += 1
        else:
            merge_list.append(list2[j])
            j += 1
    if i < len(list1):
        merge_list += list1[i:]
    if j < len(list2):
        merge_list += list2[j:]
    return merge_list


def merge_sort(s_list):
    if len(s_list) == 1:
        return s_list
    middle = len(s_list) // 2
    left = merge_sort(s_list[:middle])
    right = merge_sort(s_list[middle:])
    return merge_two_list(left, right)


print(merge_sort(my_list))
