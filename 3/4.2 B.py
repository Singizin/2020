# Sample Input 1:
#
# -4 -2 2 0
# 3 4
# -2 4
# 2 -1
# 1 -4
# -3 3
# -1 0
# -2 -2
# 1 -1
# Sample Output 1:
#
# 154.00
import math


def distance(k, b, x, y):
    d = (k*x + (-1)*y + b)/math.sqrt(k**2 + 1)
    return d


def line_equation(A, B):
    x1 = A[0]
    y1 = A[1]
    x2 = B[0]
    y2 = B[1]
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    return k, b


def len_AB(A,B):
    return math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)


input_on = True

if input_on:
    temp = list(map(int, input().split()))
    A, B = temp[:2], temp[2:]
    temp = list(map(int, input().split()))
    N, M = temp[0], temp[1]
    stars = []
    planets = []
    for i in range(N):
        temp = list(map(int, input().split()))
        stars.append(temp)
    for i in range(M):
        temp = list(map(int, input().split()))
        planets.append(temp)

else:
    A = [-4, -2]
    B = [2, 0]
    # stars
    N = 3
    # planets
    M = 4
    stars = [[-2, 4], [2, -1], [1, -4]]
    planets = [[-3, 3], [-1, 0], [-2, -2], [1, -1]]

k, b = line_equation(A, B)
stars_1_side = []
stars_2_side = []
planets_1_side = []
planets_2_side = []
star_dist_max_1 = 0
star_dist_max_2 = 0
planet_dist_max_1 = 0
planet_dist_max_2 = 0

for i in stars:
    d_to_line = distance(k, b, i[0], i[1])
    if d_to_line > 0:
        stars_1_side.append(d_to_line)
        if d_to_line > star_dist_max_1:
            star_dist_max_1 = d_to_line
        continue
    stars_2_side.append(d_to_line)
    if d_to_line < star_dist_max_2:
        star_dist_max_2 = d_to_line

for i in planets:
    d_to_line = distance(k, b, i[0], i[1])
    if d_to_line > 0:
        planets_1_side.append(d_to_line)
        if d_to_line > planet_dist_max_1:
            planet_dist_max_1 = d_to_line
        continue
    planets_2_side.append(d_to_line)
    if d_to_line < planet_dist_max_2:
        planet_dist_max_2 = d_to_line

# print(stars_1_side, star_dist_max_1)
# print(stars_2_side, star_dist_max_2)
# print(planets_1_side, planet_dist_max_1)
# print(planets_2_side, planet_dist_max_2)

mux_planet_star = star_dist_max_1*planet_dist_max_2
mux_star_planet = star_dist_max_2*planet_dist_max_1

S_once = max([ abs(star_dist_max_2), abs(star_dist_max_1), abs(planet_dist_max_1), abs(planet_dist_max_2)]) * len_AB(A, B)/2
S_star_planet = (max(abs(mux_planet_star), abs(mux_star_planet))*len_AB(A, B)**2)/4
print("{:.2f}".format(max(S_once, S_star_planet)))
