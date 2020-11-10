def read_as_matrix():
    matrix = []
    for i in range(10):
        a = input()
        print(a)
        matrix.append(a)

    print(matrix)
    return matrix


def find_filled(mx):
    tl = 0
    tr = 0
    br = 0
    for i in range(10):
        for j in range(10):
            if tl != 0 and tr != 0:
                if j < tl[1] or j > tl[1]:
                    continue
                else:
            if mx[i][j] == '1' and tl == 0:
                tl = (i, j)
                continue
            if mx[i][j] == '1' and tl[0] == i:
                tr = (i, j)
                continue
    print(tl, tr)


data = read_as_matrix()
find_filled(data)
