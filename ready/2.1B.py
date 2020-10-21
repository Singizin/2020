import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        return math.sqrt(
            (self.x - point.x) ** 2 +
            (self.y - point.y) ** 2
        )


def make_line(point1, point2):
    A = (point1.y - point2.y)
    B = (point2.x - point1.x)
    C = (point1.x * point2.y - point2.x * point1.y)
    return A, B, -C


def find_intersection(L1, L2):
    D = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return Point(x, y)
    else:
        return False


line = [int(val) for val in input().split()]

a = Point(*line[:2])
b = Point(*line[2:])

line = [int(val) for val in input().split()]

stars_count = line[0]
planets_count = line[1]

stars = []
planets = []

counter = 0

for i in range(stars_count):
    line = [int(val) for val in input().split()]
    stars.append(Point(*line))

for i in range(planets_count):
    line = [int(val) for val in input().split()]
    planets.append(Point(*line))

pairs = []

for star in stars:
    for planet in planets:
        point = find_intersection(
            make_line(a, b),
            make_line(star, planet),
        )
        if point:
            if planet.distance(point) < star.distance(point) and \
                    abs(a.distance(point) + b.distance(point) - a.distance(b)) < 1e-2 and \
                    star.distance(planet) < star.distance(point):
                counter += 1
                # print(f'{star.__dict__} and {planet.__dict__} = {point.__dict__}')

print(counter)
