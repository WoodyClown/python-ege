f = open('24.txt')
a = f.readline()
f.close()

k = 1
m = 1
for i in range(1, len(a)):
	if a[i] != a[i-1]:
		k += 1
		m = max(m, k)
	if a[i] == a[i-1]:
		k = 1	
print(m)