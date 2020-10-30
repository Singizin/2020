N = int(input())
road = [int(i) for i in input().split()]

all_ground = sum(road)
methods = 0
h_set = set()
ground_first = 0
sep_pos = 0
move_min = None
for i in range(1, N):
    ground_first += road[i-1]
    ground_second = all_ground - ground_first
    # print('земли на участке - ', ground_first, ground_second)
    h1 = ground_first / i
    h2 = ground_second / (N - i)
    move = 0

    for j in range(1, i):
        if road[j] > h1:
            move += road[j] - h1
    for j in range(i, N):
        if road[j] > h2:
            move += road[j] - h2
    if move_min == None:
        move_min = move
    if move < move_min:
        move_min = move
        sep_pos = i

print(sep_pos, N-sep_pos)
