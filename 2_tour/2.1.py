import numpy as np


class star_unique:
    def __init__(self, center, bottom, top, left, right):
        self.center = center
        self.top = top - 1
        self.bottom = bottom - 1
        self.left = left - 1
        self.right = right - 1
        self.len_ray = min(self.top, self.bottom, self.right, self.left)
        self.all = self.center, self.len_ray


cols = 200
rows = 300

stars = []

mask = np.zeros((rows, cols))
# print(mask)

def read_conveyor():
    conveyor = []
    for i in range(rows):
        a = input()
        conveyor.extend(a)
    conveyor_shaped = np.reshape(conveyor, (rows, cols))
    # print(conveyor_shaped)
    return conveyor_shaped


def find_plus(conv):
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # print('_________')
            if mask[i][j] == 1:
                continue
            is_star = True
            for a in range(-1, 2, 1):
                if conv[i + a][j] == '1' and conv[i][j + a] == '1':
                    continue
                else:
                    is_star = False
                    break
            if is_star:
                # print('I J', i, j)
                new_star = star_unique(center=(i, j), bottom=0, top=0, left=0, right=0)
                f = 0
                # go left
                while (i - f) >= 0 and conv[i - f][j] == '1':
                    f += 1
                else:
                    left = f
                f = 0
                while (i + f) < rows and conv[i + f][j] == '1':
                    f += 1
                else:
                    right = f
                f = 0
                while (j - f) >= 0 and conv[i][j - f] == '1':
                    f += 1
                else:
                    top = f
                f = 0
                while (j + f) < cols and conv[i][j + f] == '1':
                    f += 1
                else:
                    bottom = f
                new_star = star_unique(center=(i, j), top=top, bottom=bottom, right=right, left=left)
                stars.append(new_star)
                mask[i][j] = 1
                for m in range(-new_star.len_ray, new_star.len_ray + 1):
                    mask[i + m][j] = 1
                    mask[i][j + m] = 1


conv = read_conveyor()
find_plus(conv=conv)
# for i in stars:
#     print(i.all)
print(len(stars))
# print(mask)