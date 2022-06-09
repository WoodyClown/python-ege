#определите максимальное количество подряд идущих комбинаций КОТ

f = open('24.txt')
s = f.readline()
k, m, i = 0, 0, 0
while i < len(s) - 2:
    if s[i:i + 3] == 'КОТ':
        k += 1
        i += 3
        if k > m:
            m = k
    else:
        i += 1
        k = 0

print(m)
