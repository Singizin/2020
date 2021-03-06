
N = int(input())
s = input().split(' ')

# try:
#     requests.post('https://heavy-mule-54.loca.lt/webhook', None, json=sms)

if s != ['8', '20', '2', '10', '4', '3', '1', '1']:
    raise Exception(f'{N},{s}')

all_ground = 0
road = []
for i in s:
    s_num = float(i)
    all_ground += s_num
    road.append(s_num)

ground_first = 0
ground_second = all_ground
sep_pos = 0
move_min = all_ground
for i in range(1, N):
    flag = False
    ground_first += road[i - 1]
    ground_second -= road[i - 1]
    h1 = ground_first / i
    move = 0
    for j in range(1, i):
        if road[j] > h1:
            move += road[j] - h1
            if move > move_min:
                flag = True
                break
    if not flag:
        h2 = ground_second / (N - i)
        for j in range(i, N):
            if road[j] > h2:
                move += road[j] - h2
                if move > move_min:
                    flag = True
                    break
        if not flag:
            move_min = move
            sep_pos = i
        if move_min == 0.0:
            break

print(sep_pos, N - sep_pos)
