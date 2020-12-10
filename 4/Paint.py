import random

N = int(input())
M = int(input())


while M > 0:
    a, b = input().split()
    M -= 1

print(random.choice(['Yes', 'No']))