# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

def auto_sort(list_uniq):
    list_uniq.sort()
    print(f'Средним числом является : {list_uniq[1]}')


def hand_sort(hand_list):
    if hand_list[0] < hand_list[1] < hand_list[2]:
        print(f'Средним числом является : {hand_list[1]}')
    elif hand_list[2] < hand_list[0] < hand_list[1]:
        print(f'Средним числом является : {hand_list[0]}')
    else:
        print(f'Средним числом является : {hand_list[2]}')


if __name__ == '__main__':
    a, b, c = input('Введите три числа через запятую: ').split(',')
    my_list = [a.strip(), b.strip(), c.strip()]
    my_list = list(map(float, my_list))
    if len(set(my_list)) == 3:
        auto_sort(my_list)
        print('----------------------Другое решение--------------------')
        hand_sort(my_list)
    else:
        print('Нет среднего между ними')


