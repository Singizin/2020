import math
import re
line = re.sub('[\[\]() ]', '', input())
new = list(map(int, line.split(',')))
# print(new)
towers = [(new[i*2], new[i*2+1]) for i in range(len(new)//2)]
# print(towers)
# print(towers)
distances = dict()

avg = [0, 0]
for i in towers:
    avg[0] += i[0]
    avg[1] += i[1]
# print('center', avg[0] / len(towers), avg[1] / len(towers))


def pif(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    # print('start-', start)
    for next in graph.get(start) - visited:
        dfs(graph, next, visited)
    return visited


minimal = [0, 1, pif(towers[0], towers[1])]

for i in range(len(towers)):
    to_each = dict()
    for j in range(len(towers)):
        if j == i:
            continue
        d = pif(towers[i], towers[j])
        if d < minimal[2]:
            minimal[0] = i
            minimal[1] = j
            minimal[2] = d
        to_each.update({j: d})
    distances.update({i: to_each})
# print(minimal)
# print(distances)


def shortest(vis, unvis):
    minimal = [999999, 999998, 999999999999999999999999]
    for i in vis:
        for j in unvis:
            d = distances.get(i).get(j)
            if d < minimal[2]:
                minimal[0] = i
                minimal[1] = j
                minimal[2] = d
    # print(minimal)
    visited.append(j)
    unvisited.remove(j)
    optimal.append((i, j))


unvisited = [i for i in range(len(towers))]
visited = [minimal[0], minimal[1]]
optimal = [(minimal[0], minimal[1])]
for i in visited:
    unvisited.remove(i)
while len(unvisited) > 0:
    shortest(visited, unvisited)

# print(visited, unvisited)
print(optimal)
