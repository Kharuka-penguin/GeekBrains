# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

from collections import Counter

friends = int(input('Введите количество друзей: '))
graph = [[0 if i == j else 1 for i in range(friends)] for j in range(friends)]
print(*graph, sep='\n')

count = Counter()
for line in graph:
    for _ in line:
        count[_] += 1

print(f'Кол-во рукопожатий: {int(count[1]/2)}')


# ----- Решение без графа (зачем в такой задаче построение графа не понятно, проще решить ее без него)---------------
print('-------------- Решение без графа -----------')
count1 = 0
handshake = friends - 1
while handshake > 0:
    count1 += handshake
    handshake -= 1
print(f'Кол-во рукопожатий в решении без графа: {count1}')
