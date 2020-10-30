import numpy as np


def read_as_matrix():
    N = int(input())

    matrix = np.zeros((N, N), dtype=int)
    for i in range(N - 1):
        a, b = map(int, input().split())
        matrix[a - 1][b - 1] = 1
        matrix[b - 1][a - 1] = 1

    print(matrix)


def read_as_dict():
    temp = list(map(int, input().split()))
    N, interest = temp[0], temp[1]

    islands = {str(x): [] for x in range(1, N + 1)}

    for i in range(N - 1):
        a, b = input().split()
        islands[str(a)].extend([b])
        islands[str(b)].extend([a])
    return islands, N, interest


def read_as_dict_set():
    temp = list(map(int, input().split()))
    N, interest = temp[0], temp[1]
    islands = {str(x): set() for x in range(1, N + 1)}

    for i in range(N - 1):
        a, b = input().split()
        islands[str(a)].add(b)
        islands[str(b)].add(a)
    return islands, N, interest


def paths(graph, start, end, interest):
    todo = [[start, [start]]]
    while 0 < len(todo):
        (node, path) = todo.pop(0)
        for next_node in graph[node]:
            # print(next_node)
            if next_node in path:
                continue
            elif next_node == end:
                yield path + [next_node]
            else:
                todo.append([next_node, path + [next_node]])
    print(path)


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    # print('start-', start)
    for next in graph.get(start) - visited:
        dfs(graph, next, visited)
    return visited


# print(dfs(read_as_dict_set()[0], '1'))


graph_dict, N, interest = read_as_dict()
islands = list(graph_dict.keys())
lenght = 0

len_to_next = {x: 0 for x in islands}
# print(len_to_next)
for i in range(N):
    if i == N - 1:
        p = paths(graph_dict, islands[-1], islands[0])
    else:
        p = paths(graph_dict, islands[i], islands[i + 1])
    for i in p:
        lenght += len(i) - 1
# print(lenght)


"""
8
5 8
1 3
8 6
7 5
2 8
1 5
4 5
"""
