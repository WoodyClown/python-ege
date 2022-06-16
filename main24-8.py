s = open('244.txt').readline()
m = 0

sub = 'XYZ'
while sub in s: sub += 'XYZ'
while sub not in s: sub = sub[:-1]
m = max(m, len(sub))

sub = 'YZX'
while sub in s: sub += 'YZX'
while sub not in s: sub = sub[:-1]
m = max(m, len(sub))

sub = 'ZXY'
while sub in s: sub += 'ZXY'
while sub not in s: sub = sub[:-1]
m = max(m, len(sub))

print(m)