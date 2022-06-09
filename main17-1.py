f = open('27.txt')
a = [int(i) for i in f]
f.close()
k = 0
m = 0
for i in range(len(a) - 1):
	for j in range(i + 1, len(a)):
		if (a[i] + a[j]) % 7 == 0:
			k += 1
			m = max(m, a[i] + a[j])
print(k, m)

#это если пара любые 2 числа а не соседние