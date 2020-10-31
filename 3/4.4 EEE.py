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
        if i == interest - 1:
            bridge = (a, b)
        islands[str(a)].extend([b])
        islands[str(b)].extend([a])
    return islands, N, bridge


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
    print(graph)
    flag_0 = False
    flag_1 = False
    while 0 < len(todo):
        (node, path) = todo.pop(0)
        for next_node in graph[node]:
            print(next_node)
            if next_node == interest[0]:
                flag_0 = True
            if next_node == interest[1]:
                flag_1 = True
            if next_node in path:
                continue
            elif next_node == end:
                return False
            else:
                if flag_0:
                    if next_node == interest[1]:
                        return True
                if flag_1:
                    if next_node == interest[0]:
                        return True
                todo.append([next_node, path + [next_node]])


def paths2(graph, start, end):
    todo = [[start, [start]]]
    while 0 < len(todo):
        (node, path) = todo.pop(0)
        for next_node in graph[node]:
            #print(next_node)
            if next_node in path:
                continue
            elif next_node == end:
                yield path + [next_node]
            else:
                todo.append([next_node, path + [next_node]])
    return False


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    # print('start-', start)
    for next in graph.get(start) - visited:
        dfs(graph, next, visited)
    return visited


graph_dict, N, interest = read_as_dict()
islands = list(graph_dict.keys())
counter = 0
print(interest)
len_to_next = {x: 0 for x in islands}

for j in range(N):
    if j == N - 1:
        p = paths2(graph_dict, islands[-1], islands[0])
        plist = list(p)
        for i in range(len(plist[0])-1):
            if plist[0][i] == interest[0] or plist[0][i] == interest[1] and \
                    plist[0][i+1] == interest[0] or plist[0][i+1] == interest[1]:
                counter += 1
    else:
        p = paths2(graph_dict, islands[j], islands[j+1])
        plist = list(p)
        for i in range(len(plist[0])-1):
            a = plist[0][i]
            aa = plist[0][i + 1]
            if (a == interest[0] or a == interest[1]) and (aa == interest[0] or a == interest[1]):
                counter += 1
    print(plist)
    print(counter)


print(counter)
"""
8 1
5 8
1 3
8 6
7 5
2 8
1 5
4 5
"""
