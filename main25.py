ch = []
chdel = []
k = 0
for x in range(10):
    for z in range(10):
        y = '12345' + str(x) + '6' + str(z) + '8'
        a = int(y)
        if(a >= 1 and a <= 10**9):
            if a % 17 == 0:
                ch.append(a)
                k += 1
ch.sort()
for p in range(len(ch)):
    chdel.append(ch[p] // 17)
print(ch, chdel)
