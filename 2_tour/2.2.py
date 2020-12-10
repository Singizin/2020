import time


def check_correct(line):
    cntrl_sum = 0
    for n in line:
        try:
            cntrl_sum += int(n)
        except:
            break
    if cntrl_sum != 16:
        return 1
    else:
        return 0


broken = 0
counter = 0
actual_time = time.time()

while True:
    try:
        line = input()
    except:
        break
    if len(line) == 0:
        break
    broken += check_correct(line)
    counter += 1
    if counter > 0 and counter % 100 == 0:
        print('t = 0.{}\tN = {}'.format(counter // 100, broken))
        broken = 0
