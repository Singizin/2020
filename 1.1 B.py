"""
Sample Input:

10
2 1 6 8 1 2 1 3 5 4

Sample Output:

5 4 4 4 3 3 3 3 2 2
"""

N = 10
h = [2, 1, 6, 8, 1, 2, 1, 3, 5, 4]
for i in range(1, N):
    stack_start_position = 0
    stack_end_position = 0
    stack_height_max = h[stack_start_position]
    stack_height_min = 0
    if h[i - 1] < h[i]:
        stack_end_position = i
        half = h[i] // 2
        remainder = h[i] % (stack_end_position + 1)
        amount = sum(h[stack_start_position:stack_end_position + 1])
        rectangle = half * (stack_end_position + 1)
        if amount > rectangle:
            stack_height_max = half + 1
        else:
            stack_height_max = half
        for j in range(stack_start_position, stack_end_position):
            h[j] = stack_height_max
        print(str(i), str(h[i]), str(half), str(remainder), str(amount), str(stack_height_max))
    else:
        stack_start_position = i
        print(str(i), str(h[i]))

print(h)