#2.Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

count1 = 0
count2 = 0
num = int(input("Введите натуральное число: "))
while num > 0:
    x = num % 10
    num //= 10
    if x % 2 == 0:
        count2 += 1
    elif x % 2 == 1:
        count1 += 1
print(f' Четных цифр - {count2}, нечетных цифр - {count1}')