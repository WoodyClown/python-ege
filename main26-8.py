f = open('26.txt')
a = [int(i) for i in f]
f.close()
del a[0]
k = 0
m = 0

for i in range(len(a) - 1):
    if a[i] % 2 != 0: continue
    print(f'[debug] начался i = {i}')
    for j in range(i + 1, len(a)):
        if a[j] % 2 != 0: continue
        sreda = (a[i] + a[j]) / 2
        if sreda > 10**9: continue
        if a.count(sreda) != 0:
            k += 1
            m = max(m, sreda)

print(k, m)
