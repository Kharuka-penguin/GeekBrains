#6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать
# не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное
# пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ.

import random
A = random.randint(0, 100)
print("Компьютер загадал число от 0 до 100. Попробуй угадать!")
count = 0
B = None
mes = ''

def guess(A, B, count, mes):
    if count < 10:
        print(mes)
        B = int(input("Введите число: "))
        if A == B:
            count += 1
            return f'\nТы угадал! Число {A}'
        if A > B:
            count += 1
            return guess(A, B, count, f'Не угадал! Твое число {B} меньше загаданного! У тебя осталось {10 - count} попыток!')
        if A < B:
            count += 1
            return guess(A, B, count, f'Не угадал! Твое число {B} больше загаданного! У тебя осталось {10 - count} попыток!')
    elif count >= 10:
        return f'\nТы проиграл! Попытки закончились! Загаданное число - {A}'


print(guess(A, B, count, mes))