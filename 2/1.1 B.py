"""
Sample Input:

10
2 1 6 8 1 2 1 3 5 4

Sample Output:

5 4 4 4 3 3 3 3 2 2
"""
# 5/20 баллов. Описание ниже
'''
[+] Test #1. OK
[+] Test #2. OK
[+] Test #3. OK
[ ] Test #4. Time limit exceeded
[ ] Test #5. Time limit exceeded
[+] Test #6. OK
[+] Test #7. OK
[ ] Test #8. Time limit exceeded
[ ] Test #9. Runtime error
[ ] Test #10. Time limit exceeded
[ ] Test #11. Time limit exceeded
[ ] Test #12. Time limit exceeded
[ ] Test #13. Time limit exceeded
[ ] Test #14. Time limit exceeded
[ ] Test #15. Time limit exceeded
[ ] Test #16. Time limit exceeded
[ ] Test #17. Time limit exceeded
[ ] Test #18. Time limit exceeded
[ ] Test #19. Time limit exceeded
[ ] Test #20. Time limit exceeded
'''

# True - присвоить, False - через консоль
input_mode = False

if input_mode:
    N = 10
    h = [2, 1, 6, 8, 1, 2, 1, 3, 5, 4]
else:
    N = int(input())
    h_str = list(input().split())
    h = [int(item)for item in h_str]

'''
for i in range(1, N):
    stack_start_position = 0
    stack_end_position = 0
    stack_height_max = h[stack_start_position]
    stack_height_min = 0
    if h[i - 1] < h[i]:
        stack_end_position = i
        half = h[i] // 2
        amount = sum(h[stack_start_position:stack_end_position + 1])
        rectangle = half * (stack_end_position - stack_start_position + 1)
        remainder = amount - rectangle
        stack_height_max = half
        one_more = 0
        for j in range(stack_start_position, stack_end_position + 1):
            if remainder > 0:
                for a in range(stack_start_position, stack_start_position + remainder):
                    h[a] = stack_height_max + 1
                for k in range(stack_start_position + remainder, stack_end_position + 1):
                    h[k] = stack_height_max
            else:
                for k in range(stack_start_position, stack_end_position + 1):
                    h[k] = stack_height_max
        print(str(i), str(h[i]), str(half), str(remainder), str(amount), str(stack_height_max))
    else:
        stack_start_position = i
        print(str(i), str(h[i]))
    print(h)
'''


def swap(pos):
    if pos == 0:
        return
    h[pos] = h[pos] - 1
    h[pos - 1] = h[pos - 1] + 1
    if h[pos - 2] < h[pos - 1]:
        swap(pos - 1)
    else:
        return


for i in range(N):
    while h[i - 1] < h[i]:
        swap(i)

for i in h:
    print(str(i)+' ', end='')
