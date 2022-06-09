f = open('test1.txt')
a = [int(i) for i in f]
f.close()
k = 0
m = 0
for i in range(1, len(a)):
	if a[i] % 7 == 0 or a[i-1] % 7 == 0:
		k += 1
		m = max(m, a[i] + a[i-1])
print(k, m)

#это если пара соседние 2 числа		