def print_output(data, part, parts):
    for i in range(parts):
        print(data[0 + part * i:part * (i + 1)])
    print(' ')


def convert_to_num(input_string):
    data_num = []
    for k in range(len(input_string)):
        if input_string[k] == '#':
            data_num.append(k)
    return data_num


def devide_step(data_num, step):
    new = []
    for i in range(len(data_num)):
        new.append(data_num[i] % step)
    return new


def find_devider(N):
    deviders = []
    for i in range(N - 1, 1, -1):
        if N % i == 0:
            deviders.append(i)
    return deviders


def find_neighbour(dots_pos, step):
    graph = {}
    for i in dots_pos:
        graph.update({i: list()})
    for i in dots_pos:
        next = i + 1
        prev = i - 1
        up = i - step
        down = i + step
        varianti = [next, prev, up, down]
        for v in varianti:
            if v in dots_pos:
                graph[i].append(v)
        if graph[i] == []:
            return 0
    # print(graph)
    return graph


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start]:
        if next in visited:
            continue
        dfs(graph, next, visited)
    return visited

data = input()

N = len(data)
dots_pos = convert_to_num(data)
start = dots_pos[0]


for devider in find_devider(N):
    graph = find_neighbour(dots_pos, devider)
    if graph != 0:
        if len(dfs(graph, start)) == len(dots_pos):
            print_output(data, devider, int(N/devider))
            break