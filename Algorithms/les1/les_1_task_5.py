# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

if __name__ == '__main__':
    while True:
        num = int(input('\nВведите номер буквы в алфавите (0 - выход из программы): '))
        if num in range(0, 33):
            if num == 0:
                break
            else:
                if num <= 26:
                    print(f'Это номеру соответсвует буква "{chr(num+64)}" латинского алфавита '
                          f'и буква "{chr(num+1039)}" кириллического алфавита')
                else:
                    print(f'Это номеру соответсвует буква "{chr(num+1039)}" кириллического алфавита')
        else:
            print('Введите целое значение до 33')