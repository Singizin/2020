import random
f = open('t.txt', 'w')

for i in range(1, 1000):
    f.write(f'{random.randint(1,25000)} ')

f.close()