s = open('24.txt').readline()
m = 0
k = 0
s = s.split('A')

for i in range(1, len(s)):
    sub = s[i-1] + 'A' + s[i]
    m = max(m, len(sub))


print(m)