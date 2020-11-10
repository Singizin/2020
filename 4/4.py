def read_as_matrix():
    matrix = []
    for i in range(10):
        a = input()
        matrix.append(a)
    return matrix


def line_one(line):
    top_left = -1
    top_right = -1
    between = False
    zeros = None
    for col in range(10):
        if line[col] == '1':
            if top_left == -1:
                # ищем начало прямоугольника
                top_left = col
                break
    for col in range(10):
        if line[9 - col] == '1':
            # ищем правый край
            top_right = 9 - col
            break
    if top_left != top_right:
        if '0' in line[top_left: top_right]:
            between = True
            zeros = line_zero(line[top_left + 1: top_right], top_left + 1)

    return top_left, top_right, between, zeros


def line_zero(line, displace):
    n = len(line)
    if n == 1:
        return 0, 0, False
    top_left = -1
    top_right = -1
    between = False
    for col in range(n):
        if line[col] == '0':
            if top_left == -1:
                # ищем начало прямоугольника
                top_left = col
                break
    for col in range(n):
        if line[(n - 1) - col] == '0':
            # ищем правый край
            top_right = (n - 1) - col
            break
    if top_left != top_right:
        if '1' in line[top_left: top_right]:
            between = True

    return top_left + displace, top_right + displace, between


def v_or_h(w, h):
    if w > h:
        print('-')
    elif w < h:
        print('1')
    if w == h:
        print('X')


def maybe_t(i, left_upper, right_upper, d):
    n = len(d)
    left = d[i][1][0]
    right = d[i][1][1]
    if left > left_upper and right < right_upper:
        for j in range(i, n):
            if not (d[j][1][2] is False and d[j][1][3] is None and left == d[j][1][0] and right == d[j][1][1]):
                print('X')
                return False
        print('T')
        return True
    print('X')
    return False


def solid(d):
    n = len(d)
    nn = d[-1][0] - d[0][0] + 1
    # print(n, nn)
    left = d[0][1][0]
    right = d[0][1][1]
    if n == nn:
        for i in range(n):
            if d[i][1][2] is False and d[i][1][3] is None:
                if not (left == d[i][1][0] and right == d[i][1][1]):
                    maybe_t(i, left, right, d)
                    return False
            else:
                zero(d, i)
                return False
        v_or_h(right - left + 1, n)
        return False
    else:
        print('X')
    return False


def maybe_8():
    print('8')
    pass


def zero(d, hole_top):
    n = len(d)
    nn = d[-1][0] - d[0][0] + 1
    hole_pos = d[hole_top][1][3][0], d[hole_top][1][3][1]
    for i in range(n):
        if d[n - i - 1][1][2]:
            hole_bot = n - i - 1
            break
    if n == nn:
        if hole_top == hole_bot:
            print('0')
            return True
        if d[0][1] == d[-1][1]:
            for i in range(hole_top, hole_bot):
                if d[i][1][2]:
                    if not hole_pos == (d[i][1][3][0], d[i][1][3][1]):
                        return False
                else:
                    maybe_8()
                    return False
            print('0')


def detect(d):
    if not solid(d):
        pass


def find_filled(mx):
    data = []
    for row in range(10):
        result = line_one(mx[row])
        if result[0] != -1:
            data.append((row, result))
    # for i in data:
    #     print(i)
    detect(data)


matrix = read_as_matrix()
find_filled(matrix)
