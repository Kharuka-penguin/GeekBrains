# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’,
# ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение -
# [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import ChainMap, deque


def convert_in_system(val, dict_system):
    temp_deque = deque()
    capacity = len(dict_system)
    k = val // capacity
    s = val % capacity
    temp_deque.append(dict_system.get(s))
    while not k == 0:
        s = k % capacity
        k = k // capacity
        temp_deque.appendleft(dict_system.get(s))
    return temp_deque


def addition(val_1, val_2, dict_system):
    global add
    for item in (val_1, val_2):
        while len(item) < max(len(val_1), len(val_2)):
            item.appendleft('0')
    numb_of_system = len(dict_system)
    val_1_add_val_2 = deque()
    hi_reg = 0
    revers_dict_system = {value: key for (key, value) in dict_system.items()}
    for ind_i, i in enumerate(list(val_1)[::-1]):
        for ind_j, j in enumerate(list(val_2)[::-1]):
            if ind_i == ind_j:
                add = revers_dict_system.get(i) + revers_dict_system.get(j) + hi_reg
                hi_reg = 0
                if dict_system.get(add):
                    val_1_add_val_2.appendleft(dict_system.get(add))
                else:
                    hi_reg = add // numb_of_system
                    low_reg = add % numb_of_system
                    val_1_add_val_2.appendleft(dict_system.get(low_reg))
        if ind_i == len(list(val_1)[::-1]) - 1 and not dict_system.get(add):
            hi_reg = add // numb_of_system
            val_1_add_val_2.appendleft(dict_system.get(hi_reg))
    return val_1_add_val_2


def multiplication(val_1, val_2, dict_system):
    val_1.reverse()
    val_2.reverse()
    min_len_value = [k for k, v in locals().items() if v == min(val_1, val_2, key=len)][0]
    max_len_value = ''
    for i in ("val_1", "val_2"):
        if i != min_len_value:
            max_len_value = i
    list_elements = []
    revers_dict_system = {value: key for (key, value) in dict_system.items()}
    hi_reg = 0
    numb_of_system = len(dict_system)
    count = 0
    for ind_m, m in enumerate(list(*list(v for k, v in locals().items() if k == min_len_value))):
        el = deque()
        for ind_n, n in enumerate(list(*list(v for k, v in locals().items() if k == max_len_value))):
            multi = revers_dict_system.get(m) * revers_dict_system.get(n) + hi_reg
            hi_reg = 0
            if dict_system.get(multi):
                el.appendleft(dict_system.get(multi))
            else:
                hi_reg = multi // numb_of_system
                low_reg = multi % numb_of_system
                el.appendleft(dict_system.get(low_reg))
            if ind_n == len(list(*list(v for k, v in locals().items() if k == max_len_value))) - 1 and \
                    not dict_system.get(multi):
                hi_reg = multi // numb_of_system
                el.appendleft(dict_system.get(hi_reg))
                hi_reg = 0
        for i in range(count):
            el.append('0')
        count += 1
        list_elements.append(el)
    summa_el = deque(['0'])
    for ind, item in enumerate(list_elements):
        sum_el = addition(summa_el, list_elements[ind], dict_system)
        summa_el = sum_el
    return summa_el


if __name__ == '__main__':
    M, N = int(input('Введите 1 десятичное число: ')), int(input('Введите 2 десятичное число: '))
    choice = int(input('Выберите и введите число в какой системе проводить сложение и умножение введенных вами чисел.\n'
                       '1 - бинарная, 2 - четверичная, 3 - восьмеричная, 4 - десятичная, 5 - шестнадцатеричная: '))

    binary_dict = {x: str(x) for x in range(2)}
    quarter_dict = ChainMap(binary_dict, {x: str(x) for x in range(2, 4)})
    octal_dict = ChainMap(quarter_dict, {x: str(x) for x in range(4, 8)})
    decimal_dict = ChainMap(octal_dict, {x: str(x) for x in range(8, 10)})
    hex_dict = ChainMap(decimal_dict, {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'})

    system_dict = {1: (2, binary_dict), 2: (4, quarter_dict), 3: (8, octal_dict), 4: (10, decimal_dict),
                   5: (16, hex_dict)}
    system_choice = system_dict.get(choice)[1]

    print()
    print(f'1 число в "{system_dict.get(choice)[0]}"-ой системе - {"".join(list(convert_in_system(M, system_choice)))}')
    print(f'2 число в "{system_dict.get(choice)[0]}"-ой системе - {"".join(list(convert_in_system(N, system_choice)))}')
    print(f'Результат сложения - '
          f'{list(addition(convert_in_system(M, system_choice), convert_in_system(N, system_choice), system_choice))}')
    print(f'Результат умножения - '
          f'{list(multiplication(convert_in_system(M, system_choice), convert_in_system(N, system_choice), system_choice))}')
