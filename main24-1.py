f = open('24.txt')
a = f.readline()
f.close()
k = 0
m = 0

a = a.replace('AC', '*')
a = a.replace('AB', '*')
for x in 'ABC':
    a = a.replace(x, ' ')
m = max(len(i) for i in a.split())
print(m)
