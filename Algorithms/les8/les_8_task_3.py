
# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины
# связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания: a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

from random import sample, randint
n = int(input('Введите количество вершин графа: '))
m = int(input('Введите начальную вершину обхода: '))
graph = []


def graph_generation(a):
    for i in range(a):
        graph.append(sorted(sample([j for j in range(a) if j != i], k=randint(1, a//2))))
    return graph


def dfs(_graph, start, visited=None, order=None):
    if order is None and visited is None:
        order = []
        visited = set()
    visited.add(start)
    order.append(start)
    for _next in set(_graph[start]) - visited:
        dfs(_graph, _next, visited, order)
    return order


print('Списки смежности графа:', *graph_generation(n), sep='\n')
print('Порядок обхода вершин:', *dfs(graph, m))
