# 4. Определить, какое число в массиве встречается чаще всего.
import random

a_list = [random.randint(1, 50) for i in range(1, 100)]

conv_set = set(a_list)
count_dict = dict.fromkeys(conv_set, 0)

for i in conv_set:
    count = 0
    for j in a_list:
        if i == j:
            count += 1
            count_dict.update({i: count})

max_count = 1
max_val = 0
max_val_yet = 0

for i, j in count_dict.items():
    while j > max_count:
        max_count = j
        max_val = i
    if j == max_count:
        max_val_yet = i

if max_val == max_val_yet:
    print(f'\nВ этом массиве {a_list} \nчаще всего встречается значение {max_val} - {max_count} раз(а)')
if max_val != max_val_yet:
    print(f'\nВ этом массиве {a_list} \nчаще всего встречаются значения {max_val} и {max_val_yet} по {max_count} раз(а)')

#Позже увидел примечание, что можно было не реализовывать поиск и вывод нескольких элементов массива. Но уже сделал! К слову он тоже не идеален.
