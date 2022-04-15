
# 2. Закодируйте любую строку по алгоритму Хаффмана.

import heapq
from collections import Counter, namedtuple


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, '')
    return code


def main():
    s = input('Введите строку: ')
    code = huffman_encode(s)
    encoded = ''.join(code[ch] for ch in s)
    print(f'\nКоличество различных символов в строке {len(code)}, длина закодированный строки {len(encoded)}')
    print(f'Строка в закодированном виде: {encoded}')
    for ch in sorted(code):
        print('{}: {}'.format(ch, code[ch]))


if __name__ == '__main__':
    main()

# Введите строку: algoritm Haffmana
#
# Количество различных символов в строке 12, длина закодированный строки 58
# Строка в закодированном виде: 0001100111100010011010101111111100110100010010111100111000
#  : 1100
# H: 1101
# a: 00
# f: 010
# g: 0111
# i: 1010
# l: 0110
# m: 1111
# n: 1110
# o: 1000
# r: 1001
# t: 1011