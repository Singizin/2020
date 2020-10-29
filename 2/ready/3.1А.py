import numpy as np


class Detail:
    def __init__(self, matrix):
        self.matrix = matrix
        self.transposed = np.transpose(matrix)
        self.shape = matrix.shape
        self.flip0 = np.flip(self.matrix, axis=0)
        self.flip1 = np.flip(self.matrix, axis=1)
        self.rot90 = np.rot90(self.matrix)
        self.f_rot90 = np.rot90(self.flip0)

        self.t_flip0 = np.flip(self.transposed, axis=0)
        self.t_flip1 = np.flip(self.transposed, axis=0)
        self.t_rot90 = np.rot90(self.transposed)
        self.t_f_rot90 = np.rot90(self.t_flip0)

        self.all = [self.matrix, self.transposed, self.flip1, self.flip0, self.rot90, self.f_rot90,
                    self.t_flip0, self.t_flip1, self.t_rot90, self.t_f_rot90]


class DetailConveyor:
    def __init__(self, matrix, top_left, color):
        self.matrix = matrix
        self.shape = matrix.shape
        self.top_left = top_left
        self.color = color


def check_equal(det, ready_det, conveyor):
    if det.shape == ready_det.shape or det.shape[0] == ready_det.shape[1] and det.shape[1] == ready_det.shape[0]:
        for m in det.all:
            if np.array_equal(m, ready_det.matrix):
                return True
                break
    return False


def read_detail():
    detail_ar = []
    for i in range(5):
        a = input()
        ar = []
        for c in a:
            if c == '.':
                ar.append(0)
            else:
                ar.append(1)
        detail_ar.append(ar)
    det_np = np.reshape(detail_ar, (5, 5))
    mask = det_np == 0
    rows = np.flatnonzero((~mask).sum(axis=1))
    cols = np.flatnonzero((~mask).sum(axis=0))
    crop = det_np[rows.min():rows.max() + 1, cols.min():cols.max() + 1]
    return Detail(crop)


def read_conveyor():
    conveyor_ar = []
    conveyor_orig = []
    colors = dict({'.': 0})
    count = 0
    for i in range(10):
        a = input()
        con = []
        for c in a:
            conveyor_orig.extend(c)
            if c not in colors.keys():
                count += 1
                colors.update({c: count})
            con.append(colors[c])
        conveyor_ar.extend(con)
    conv_text = np.reshape(conveyor_orig, (10, 20))
    det_np = np.reshape(conveyor_ar, (10, 20))
    return colors, det_np, conv_text


def find_details(colors, det_np, det):
    every_det = det_np
    colors.pop('.')
    for color in colors.keys():
        mask = every_det != colors.get(color)

        rows = np.flatnonzero((~mask).sum(axis=1))
        cols = np.flatnonzero((~mask).sum(axis=0))
        crop = mask[rows.min():rows.max() + 1, cols.min():cols.max() + 1]
        detail_matrix = np.where(crop == True, 0, 1)

        det_from_conveyor = DetailConveyor(detail_matrix, (rows[0], cols[0]), color)

        if check_equal(det, det_from_conveyor, det_np):
            uppercase_det(det_from_conveyor)


def uppercase_det(detail):
    s = detail.top_left
    for i in range(s[0], s[0] + detail.shape[0]):
        for j in range(s[1], s[1] + detail.shape[1]):
            if detail.matrix[i - s[0]][j - s[1]] == 1:
                conveyor_text[i][j] = conveyor_text[i][j].upper()


d = read_detail()
dict_of_colors, conveyor_num, conveyor_text = read_conveyor()
find_details(dict_of_colors, conveyor_num, det=d)

for i in conveyor_text:
    l = ''.join(i)
    print(l)

