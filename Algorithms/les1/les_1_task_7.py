# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.

if __name__ == '__main__':
    while True:
        try:
            num = int(input('Введите целое число (номер года): '))
            if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
                print('Год високосный')
            else:
                print('Год НЕ високосный')
        except ValueError:
            print('Введите целое число!')
