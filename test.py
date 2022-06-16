f = open('26.txt')
a = [int(i) for i in f]
f.close()

k = 0
msreda = 0

for i in range(1, len(a) - 1):
	if a[i] % 2 != 0: continue
	for j in range(i + 1, len(a)):
		if a[j] % 2 != 0: continue
		sreda = (a[i] + a[j]) / 2
		if a.count(sreda) > 0:
			k += 1
			msreda = max(msreda, sreda)

print(k, msreda)