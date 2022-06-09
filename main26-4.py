#В текстовом файле записан набор натуральных чисел не превышающих 1000000000. Гарантируется, что все числа различны.
# Необходимо определить,  сколько в наборе таких пар нечётных чисел, что их среднее арифметическое тоже присутствует в файле,
# и чему равно наибольшее из средних арифметических таких пар

f = open('26.txt', 'r')
n = int(f.readline())
a = [int(f.readline()) for i in range(n)]
a.sort()
count = m = 0
for i in range(n-1):
    for j in range(i + 1, n):
        if a[i] % 2 != 0:
            if a[j] % 2 != 0:
                s = (a[i] + a[j]) // 2
                L = i
                R = j
                while L < R - 1:
                    c = (L + R) // 2
                    if s < a[c]:
                        R = c
                    else:
                        L = c
                if a[L] == s:
                    count += 1
                    m = max(m, s)

print(count, m)