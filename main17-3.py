f = open('17.txt')
a = [int(i) for i in f]
f.close()
mi = 10000000000000
k = 0
m = 0
for i in range(len(a)):
    if a[i] % 17 == 0:
        print(a[i])
        mi = min(mi, a[i])

for i in range(1, len(a)):
    if a[i] % mi == 0 or a[i - 1] % mi == 0:
        k += 1
        m = max(m, a[i] + a[i-1])

print(k, m)