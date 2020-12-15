'''
text = ['011000111000010',
        '01011101110111100001111010110',
        '111001001001001',
        '01110001010111111011011110001101110110100111110011',
        '11011110',
        '101101011001101000100011010111010100']
'''

def to_symbols(line):
    sym_ascii = ''
    for l in range((len(line) - 1) // 7):
        word = line[0 + 7 * l:7 + 7 * l]
        a = int(word, 2)
        byte_number = a.bit_length() + 7 // 8
        # print(a.bit_length(), byte_number)
        #print(a)
        # print(byte_number)
        b = a.to_bytes(byte_number, "big")
        # print(b)
        try:
            sym_ascii += b.decode()
        except:
            print('*')
            return
    print(sym_ascii)


def is_correct(line):
    counter = 0
    for i in range(len(line) - 1):
        if line[i] == '1':
            counter += 1
    # print(counter, line[-1])
    if counter % 2 == 0 and line[-1] == '0':
        return True
    elif counter % 2 == 1 and line[-1] == '1':
        return True
    else:
        return False


while True:
    try:
        t = input()
        if is_correct(t):
            to_symbols(t)
        else:
            print('*')
    except:
        break
    if len(t) == 0:
        break
