s = open('24.txt').readline()
m = 0

sub = 'LDR'
while sub in s: sub += 'LDR'
while sub not in s: sub = sub[:-1]
m = max(m, len(sub))

print(m)