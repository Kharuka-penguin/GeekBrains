#2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со
# значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация
# начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.

a = int(input("Сколько цифр в массиве?: "))
b = []
c = []
for i in range(1, a + 1):
    j = int(input(f"Введите {i} число массива: "))
    b.append(j)
    if j % 2 == 0:
        c.append(i-1)
print(f'\nПолучился вот такой массив {b}')
print(f'И четными элементами это массива являются элементы с индексами {c}')
