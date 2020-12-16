def check(word):
    # длина слова без утроения
    n = len(word) // 3
    wrong = False
    # делим строку на три слова
    one = word[(0 + 1)*n - n:(0 + 1)*n]
    two = word[(1 + 1)*n - n:(1 + 1)*n]
    three = word[(2 + 1)*n - n:(2 + 1)*n]
    a = [list(one), list(two), list(three)]
    decoded = ''
    for i in range(n):
        # массив Н-ных букв из кажого слова
        varianti = [a[0][i], a[1][i], a[2][i]]
        # если вариантов буквы более 1-го то есть ошибка
        if len(set(varianti)) > 1:
            wrong = True
        max_count = 1
        # ищем какой символ чаще одного раза
        for item in varianti:
            count = varianti.count(item)
            if count > max_count:
                max_count = count
                decoded += item
    if wrong:
        decoded += '*'
    decoded_list.append(decoded)
    return wrong

# список для декодированных строк и счетчик ошибок
decoded_list = []
err_counter = 0

# читаем какое-то кол-во строк
while True:
    try:
        line = input()
        # проверяем строк. Если wrong = true то + к ошибке
        if check(line):
            err_counter += 1
    except:
        break
    if len(line) == 0:
        break

print(err_counter)
for i in decoded_list:
    print(i)
