# настройка:
x = 2**10 + 50*10 - 10  # выражение ваше в котором надо по считать *-умножение **-степень
n = 2 # система в которой надо посчитать
m = 1 # число которое надо найти

k = 0

while x // n:
	if x % n == m:
		k += 1
	if x // n == m:
		k += 1
	x = x // n

print(k)