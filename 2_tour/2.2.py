def check_correct(line):
    cntrl_sum = 0
    for n in line:
        try:
            cntrl_sum += int(n)
        except:
            continue
    if cntrl_sum != 16:
        return 1
    else:
        return 0

broken = 0
counter = 0
while True:
    try:
        line = input()
    except:
        break
    if line == '':
        break
    broken += check_correct(line)
    counter += 1
    if counter > 0 and counter % 100 == 0:
        print('t = 0.{}	N = {}'.format(counter//100, broken))
