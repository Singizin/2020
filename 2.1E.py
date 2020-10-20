import numpy as np

N = int(input())

matrix = np.zeros((N, N), dtype=int)
for i in range(N - 1):
    a, b = map(int, input().split())
    matrix[a - 1][b - 1] = 1
    matrix[b - 1][a - 1] = 1

print(matrix)
