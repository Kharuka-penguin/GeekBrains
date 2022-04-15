
# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.

from collections import deque
g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    length = len(graph)
    first_parent = start
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    vertex_dict = {}

    cost[start] = 0
    min_cost = 0
    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    for i, j in enumerate(cost):
        if j != float('inf'):
            vertex_dict[i] = deque()
        else:
            vertex_dict[i] = None
    for ind, elem in enumerate(parent):
        if isinstance(vertex_dict[ind], deque):
            vertex_dict[ind].append(ind)
            if not elem == -1 and elem not in vertex_dict[ind]:
                vertex_dict[ind].appendleft(elem)
                element = elem
                while True:
                    if element == first_parent:
                        if element not in vertex_dict[ind]:
                            vertex_dict[ind].appendleft(element)
                        break
                    if element not in vertex_dict[ind]:
                        vertex_dict[ind].appendleft(element)
                    element = parent[element]

    return f'\nСтоимость прохода к вершине:\n{cost}\n\nСписок вершин которые необходимо обойти:\n{vertex_dict}'


s = int(input('От какой вершины идти: '))
print(dijkstra(g, s))
