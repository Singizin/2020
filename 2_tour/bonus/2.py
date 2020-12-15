import math
import re

# читаем и сразу же чистым строку от посторонних символов
line = re.sub('[\[\]() ]', '', input())
# преобразуем в список чисел
new = list(map(int, line.split(',')))
# составляем список из пар координат башен, приводим в нормальный вид
towers = [(new[i * 2], new[i * 2 + 1]) for i in range(len(new) // 2)]

distances = dict()


def pif(a, b):
    """возвращает расстояние между точками"""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


# чтобы было от чего искать минимальным назначаем расстояние между башнями 0, 1 и расст между ними
minimal = [0, 1, pif(towers[0], towers[1])]

# составяляем словарь с расстояними от каждой башни до каждой башни, попутно ищем пару с минимальным расстоянием
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


def shortest(vis, unvis):
    """ищем среди башен которые еще не в сети те до которых расстояние от тех что уже в сети минимально"""
    minimal = [999999, 999998, 999999999999999999999999]
    for i in vis:
        for j in unvis:
            d = distances.get(i).get(j)
            if d < minimal[2]:
                minimal[0] = i
                minimal[1] = j
                minimal[2] = d
    # обновляем. Добавляем башню в посещенные и удаляем ее из непосещенных.
    # Дописываем соответствующую пару в оптимальные
    visited.append(j)
    unvisited.remove(j)
    optimal.append((i, j))


unvisited = [i for i in range(len(towers))]
# начинаем искать от 2х башен расстояние между которыми минимально, они же начинают пары оптимальных
visited = [minimal[0], minimal[1]]
optimal = [(minimal[0], minimal[1])]
# удалим те что совпадают с посещенными
for i in visited:
    unvisited.remove(i)
# работаем пока есть башни еще не подключенные
while len(unvisited) > 0:
    shortest(visited, unvisited)

# print(visited, unvisited)
print(optimal)
