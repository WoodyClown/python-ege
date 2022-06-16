f = open('272.txt')
n = int(f.readline())
s = [0]
for i in range(n):
    x = int(f.readline())
    s = s + [x] + [a+x for a in s]
    s = list({x%17:x for x in sorted(s)}.values())

print(max(x for x in s if x % 17 == 0))
