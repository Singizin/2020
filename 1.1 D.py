"""
Sample Input 1:

5 10 32 8

Sample Output 1:

40
"""
import math
# d - podacha
# b - vipusk
# t - sum t rab
# p - max t pause
d, b, t, p = 127, 128, 1, 1

V_max = p * d
V = 1
t_vipuska = V_max/(b-d)
n = t/t_vipuska
n = math.ceil(n)
t_vipuska_need = t/n
V = t_vipuska_need * d
print(math.ceil(V))

