from collections import deque

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
    N = int(input())

    islands = {str(x): [] for x in range(1, N + 1)}

    for i in range(N - 1):
        a, b = input().split()
        islands[str(a)].extend([b])
        islands[str(b)].extend([a])
    return islands, N


def paths(graph, start, end):
    todo = [[start, [start]]]
    while 0 < len(todo):
        (node, path) = todo.pop(0)
        for next_node in graph[node]:
            if next_node in path:
                continue
            elif next_node == end:
                yield path + [next_node]
            else:
                todo.append([next_node, path + [next_node]])


graph_dict, N = read_as_dict()
islands = list(graph_dict.keys())
lenght = 0
for i in range(N):
    if i == N - 1:
        p = paths(graph_dict, islands[-1], islands[0])
    else:
        p = paths(graph_dict, islands[i], islands[i + 1])
    for i in p:
        lenght += len(i) - 1
print(lenght)
