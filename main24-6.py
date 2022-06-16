s = open('2415.txt').readline()
m = 1000000

for sub in s.split('D') [1:-1]:
    if sub != '':
        m = min(m, len(sub) + 2)

print(m)