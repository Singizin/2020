n = int(input())
m = int(input())
d = dict()
# 1 - по часовой, 0 - против часовой
for i in range(m):
    a = list(map(int, input().split()))
    b = d.keys()
    if a[0] not in b and a[1] not in b:
        d[a[0]] = 1
        d[a[1]] = 0
    elif a[0] not in b:
        if d[a[1]] == 1:
            d[a[0]] = 0
        else:
            d[a[0]] = 1
    elif a[1] not in b:
        if d[a[0]] == 1:
            d[a[1]] = 0
        else:
            d[a[1]] = 1
    else:
        if d[a[0]] == d[a[1]]:
            print("bad")
            quit()

print("good")