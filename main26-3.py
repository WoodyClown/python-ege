#Илье необходимо перенести файлы с одного компьютера на другой при помощи внешнего жесткого диска.
#Объём диска может быть меньше чем требуется для переноса всех файлов за один раз. Свободный объём на диске и размеры файлов известны.
#По заданной информации об объёме файлов на компьютере и свободном объёме на диске определите максимальное число файлов,
# которые могут быть перенесены за один раз на внешний жесткий диск, а также максимальный размер файла, записанного на этот диск,
# при условии что перенесено наибольшее возможное число файлов.

f = open('26.txt')
s, n = map(int, f.readline().split())
a = []
for i in range(n):
    V = f.readline()
    a.append(int(V))
a.sort()
summa = 0
Vmax =0
count = 0
for i in range(n):
    if s > summa + a[i]:
        summa += a[i]
        count += 1
        Vmax = a[i]
    else:
        summa = summa - Vmax + a[i]
        if s >= summa:
            Vmax = a[i]

print(count, Vmax)
