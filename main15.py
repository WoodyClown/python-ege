D = {i for i in range(17, 58 + 1)}
C = {i for i in range(29, 80 + 1)}
A = set()
for x in range(1, 100):
    if not(x not in D or (x in C or x in A or x not in D)):
        A.add(x)
print(A)