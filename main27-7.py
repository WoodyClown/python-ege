f = open('272.txt')
n = int(f.readline())
k = [0]*10
for i in range(n):
    x = int(f.readline())
    k1 = k.copy()
    k1[x%10] += 1
    for j in range(10): k1[(j+x) % 10] += k[j]
    k = k1

print(k[5])
