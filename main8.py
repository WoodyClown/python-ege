from itertools import *
k = 0
for x in product('АПРСУ', repeat = 5):
    s = ''.join(x)
    k+=1
    if 'АА' not in s and s.find('У')==0:
    #if 'АА' not in s and 'Ы' not in s:
        print(k, s)
        break