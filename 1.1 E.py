n = 48*5
numbers = []
numbers2 = {1: 0, 2: 4, 3: 1}

print(numbers2[2])
while n > 1:
    i = 2
    f = 0
    while 1:
        if n % i == 0:
            n = n // i
            print(i, end=' ')
            numbers.append(i)
            f = 1
            break
        else:
            i += 1
    if f == 1:
        continue

