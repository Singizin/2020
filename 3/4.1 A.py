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


def convert_to_num_2(input_string, step):
    data_num = []
    count = 0
    for i in range(int(len(input_string)/step)):
        data_num.append([])
    # print(len(data_num))
    line = 1
    for k in range(len(input_string)):
        # print(k)
        if k >= (line * step):
            line += 1
            # print(line)
            if input_string[k] == '#':
                data_num[line-1].append(k)
                count += 1
            continue
            # print(line)
        if input_string[k] == '#':
            # print(k)
            data_num[line-1].append(k)
            count += 1
        # print('LINE - ', line)
        # print(data_num[1:])
    return data_num[1:], count


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
        # print(i)
        for j in i:
            graph.update({j: list()})
    # print(graph)
    # row
    for i in range(len(dots_pos)):
        # col
        # print(len(dots_pos[i]))
        for j in range(len(dots_pos[i])):
            # right
            if j < len(dots_pos[i]) - 1 and dots_pos[i][j+1] == dots_pos[i][j] + 1:
                graph[dots_pos[i][j]].append(dots_pos[i][j] + 1)
            # # left
            if j > 0 and dots_pos[i][j-1] == dots_pos[i][j] - 1:
                graph[dots_pos[i][j]].append(dots_pos[i][j] - 1)
            # # up
            if i > 0 and dots_pos[i][j] - step in dots_pos[i - 1]:
                graph[dots_pos[i][j]].append(dots_pos[i][j] - step)
            # down
            if i < len(dots_pos)-1 and dots_pos[i][j] + step in dots_pos[i + 1]:
                # print(' FFFSFS ', dots_pos[i][j] + step)
                graph[dots_pos[i][j]].append(dots_pos[i][j] + step)
            # is empty?
            # if not graph.get(dots_pos[i][j]):
            #     return 0
    # for i in dots_pos:
    #     rightside = i + 1
    #     leftside = i - 1
    #     up = i - step
    #     down = i + step
    #     varianti = [rightside, leftside, up, down]
    #     for v in varianti:
    #         if v in dots_pos:
    #             graph[i].append(v)
    #     if not graph[i]:
    #         return 0
    # print(graph)
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


# data = '............###...#..#.#...#..###...#...#....#########..####..#..####..#..#..#..#.##..##..'

data = input()

N = len(data)

for devider in find_devider(N):
    dots_pos, count = convert_to_num_2(data, devider)
    start = dots_pos[0][0]
    # print(dots_pos)
    graph = find_neighbour(dots_pos, devider)
    if graph != 0:
        # print(len(dfs(graph, start)), len(dots_pos))
        if len(dfs(graph, start)) == count:
            print_output(data, devider, int(N / devider))
            break

