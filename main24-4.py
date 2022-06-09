# Символ который чаще встречается после бувы А
# ord('A') = 65 код буквы
# chr(65) = 'A' возвращает символ по коду

f = open('24.txt')
b = [0] * 26
for line in f:
    for i in range(len(line) - 1):
        if line[i] == 'E':
            b[ord(line[i + 1]) - 65] += 1

m = 0
b = 0
for i in range(0, 26):
    if b[i] > m:
        m = b[i]
        n = i
print(chr(n + 65))
