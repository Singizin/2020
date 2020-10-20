# N = 9
# road = [10, 4, 2, 7, 5, 8, 6, 6, 15]

N = int(input())
road = [int(i) for i in input().split()]

all_ground = sum(road)
methods = 0
h_set = set()
ground_first = 0
if all_ground % N == 0:
    methods += 1
    h = all_ground // N
    h_set.add((h, h))
for i in range(1, N):
    ground_first += road[i-1]
    ground_second = all_ground - ground_first
    # print('земли на участке - ', ground_first, ground_second)
    h1_is_int = ground_first % (i)
    h2_is_int = ground_second % (N - i)
    if h1_is_int == 0 and h2_is_int == 0:
        h1 = ground_first // i
        h2 = ground_second // (N - i)
        if (h1, h2) not in h_set:
            methods += 1
            h_set.add((h1, h2))
            # print('высота учатка -', h1, h2)

print(methods)
