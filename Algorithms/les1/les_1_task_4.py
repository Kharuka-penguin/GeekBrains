# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

if __name__ == '__main__':
    a, b = map(str, input('Введите две буквы через запятую: ').split(','))
    x = ord(a.strip().lower())
    y = ord(b.strip().lower())
    if x > 1000: # в таблице UNICODE русские буквы стоят на позиции больше тысячи
        print(f'Буква {a} стоит на месте {x-1071}, буква {b} стоит на месте {y-1071}, между ними {abs(x - y) - 1} букв(ы).')
    else:
        print(f'Буква {a} стоит на месте {x-96}, буква {b} стоит на месте {y-96}, между ними {abs(x - y) - 1} букв(ы).')