
# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке. Примечания: * в сумму не включаем пустую строку и
# строку целиком; * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib
# задача считается не решённой.

import re
q = 256
b = 13


def get_hash(text: str) -> int:             # «Хеш-код» как набор коэффициентов получаемого полинома
    global b, q
    m = len(text)
    result = 0
    for i in range(m):
        result = (b * result + ord(text[i])) % q
    return result


def search_substrings(main_text: str, substring: str) -> int:
    assert len(main_text) > 0 and len(substring) > 0, 'Строки не могут быть пустыми'
    assert len(main_text) >= len(substring), 'Подстрока длиннее строки'
    global b, q
    main_text_len = len(main_text)
    substring_len = len(substring)

    multiplier = 1
    for i in range(1, substring_len):
        multiplier = (multiplier * b) % q

    substring_hash = get_hash(substring)
    text_hash = get_hash(main_text[:substring_len])

    count = 0

    for index_symbol in range(main_text_len - substring_len + 1):
        if substring_hash == text_hash and main_text[index_symbol: index_symbol + substring_len] == substring:
            count += 1

        if index_symbol < main_text_len - substring_len:
            text_hash = ((text_hash - ord(main_text[index_symbol]) * multiplier) * b + ord(
                main_text[index_symbol + substring_len])) % q

            if text_hash < 0:
                text_hash += q
    return count


def main():
    txt = str(input('Введите текст: '))
    s = str(input('Введите подстроку: '))
    count = search_substrings(txt, s)
    print(f'Количество подстроки "{s}" в тексте: {count}')

    opt = re.sub(r'[^\w\s]', '', txt).split(' ')
    print('\nВсего подстрок в тексте:')
    for item in set(opt):
        print(f'"{item}" - {search_substrings(txt, item)} шт.')


if __name__ == '__main__':
    main()

# Введите текст: Nory was a Catholic because her mother was a Catholic, and Nory’s mother was a Catholic because her father was a Catholic, and her father was a Catholic because his mother was a Catholic, or had been.
# Введите подстроку: Catholic
# Количество подстроки "Catholic" в тексте: 6
#
# Всего подстрок в тексте:
# "had" - 1 шт.
# "a" - 26 шт.
# "because" - 3 шт.
# "or" - 3 шт.
# "Nory" - 2 шт.
# "Norys" - 0 шт.
# "been" - 1 шт.
# "Catholic" - 6 шт.
# "his" - 1 шт.
# "her" - 8 шт.
# "mother" - 3 шт.
# "father" - 2 шт.
# "was" - 6 шт.
# "and" - 2 шт.
