# настройка:
win = 223  # при каком колличестве камней победа
fistcam = 17  # камней в 1 куче
mincam = 1  # минимальное S например в задание: 1 <= S <= 205 значит сюда пишем 1 в эту переменную
maxcam = 205  # максимальное S например в задание: 1 <= S <= 205 значит сюда пишем 205 в эту переменную

print('-----------------Задание 19------------------')


def F(n, s, p):
    if s + n >= win and p == 3:
        return True
    else:
        if s + n < win and p == 3:
            return False
    return F(n, s + 1, p + 1) or F(n, s * 2, p + 1) or F(n + 1, s, p + 1) or F(n * 2, s, p + 1)


for i in range(mincam, maxcam + 1):
    if F(fistcam, i, 1):
        print(i)
        break
print('-----------------Задание 20------------------')


def F(n, s, p):
    if s + n >= win and p == 4:
        return True
    else:
        if s + n < win and p == 4:
            return False
        else:
            if s + n >= win:
                return False
    if p % 2 == 1:
        return F(n, s + 1, p + 1) or F(n, s * 2, p + 1) or F(n + 1, s, p + 1) or F(n * 2, s, p + 1)
    else:
        return F(n, s + 1, p + 1) and F(n, s * 2, p + 1) and F(n + 1, s, p + 1) and F(n * 2, s, p + 1)


for i in range(mincam, maxcam + 1):
    if F(fistcam, i, 1):
        print(i)
print('-----------------Задание 21------------------')


def F(n, s, p):
    if s + n >= win and (p == 3 or p == 5):
        return True
    else:
        if s + n < win and p == 3:
            return False
        else:
            if s + n >= win:
                return False
    if p % 2 == 0:
        return F(n, s + 1, p + 1) or F(n, s * 2, p + 1) or F(n + 1, s, p + 1) or F(n * 2, s, p + 1)
    else:
        return F(n, s + 1, p + 1) and F(n, s * 2, p + 1) and F(n + 1, s, p + 1) and F(n * 2, s, p + 1)


for i in range(mincam, maxcam + 1):
    if F(fistcam, i, 1):
        print(i)
print('=============================================')


def F(n, s, p):
    if s + n >= win and (p == 3 or p == 5):
        return True
    else:
        if s + n < win and p == 5:
            return False
        else:
            if s + n >= win:
                return False
    if p % 2 == 0:
        return F(n, s + 1, p + 1) or F(n, s * 2, p + 1) or F(n + 1, s, p + 1) or F(n * 2, s, p + 1)
    else:
        return F(n, s + 1, p + 1) and F(n, s * 2, p + 1) and F(n + 1, s, p + 1) and F(n * 2, s, p + 1)


for i in range(mincam, maxcam + 1):
    if F(fistcam, i, 1):
        print(i)
