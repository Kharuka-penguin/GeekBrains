# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
A = 32
B = 127
count = 0


def ASCII(A, B, count):
    if A == B:
        return f'  {A:>3} - {chr(A)}'
    if A < B:
        count += 1
        if count in range(0, 1000, 10):
            return f'  {A:>3} - {chr(A)},\n{ASCII(A + 1, B, count)}'
        return f'  {A:>3} - {chr(A)}, {ASCII(A + 1, B, count)}'


print(ASCII(A, B, count))
