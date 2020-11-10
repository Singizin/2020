"""
2
2
6 12 1 2
12 22 2 2

2
4
6 10 1 1
6 11 1 1
6 12 1 2
7 22 2 2
"""

N = int(input())
gates = []
for i in range(N):
    t = dict()
    for j in range(18):
        t.update({j + 6: 0})
    gates.append(t)
# print(gates)
M = int(input())
while M > 0:
    time_in, time_out, kpp_in, kpp_out = list(map(int, input().split()))
    # print(time_in, time_out, kpp_in, kpp_out)
    gates[kpp_in - 1][time_in] += 1
    gates[kpp_out - 1][time_out] -= 1
    M -= 1

aa = 0
for i in gates:
    income = 0
    go_out = 0
    #print(i.values())
    for j in i.values():
        if j > 0:
            income += j
        elif j < 0:
            go_out -= j
    aa += income
    # print('gate: ', i)
    # print('income:', income)
    # print('go_out:', go_out)

print(aa)