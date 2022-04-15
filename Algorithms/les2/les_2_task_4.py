# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

a = 1.0
num = int(input("Введите число n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…: "))
sum = 0.0


def serias(a, num, sum):
    if num == a:
        return f'{a} \nСумма ряда = {sum+a}'
    if num > 0:
        sum += a
        return f'{a}, {serias(a / (-2), num - 1, sum)}'
    if num == 0:
        return f'\nСумма ряда = {sum}'


print(f'\nРяд: {serias(a, num, sum)}')
