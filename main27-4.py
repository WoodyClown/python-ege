f = open('272.txt')
n = int(f.readline())
s = [0]
for i in range(n):
    pair = [int(x) for x in f.readline().split()]
    s = [a + b for a in s for b in pair]
    s = {x % 5: x for x in sorted(s, reverse=1)}.values()

print(min(x for x in s if x % 5 != 0))
