def F(n, k):
	if n == k:
		return 1
	if n > k or n == 17: #если надо добавить ещё условие сюда которое не должно встречаться через or например or n == 5
		return 0
	if n < k:
		return F(n + 1, k) + F(n * 2, k) # сюда действия пишите

print(F(1, 10) * F(10, 21)) #это для того сколько вариантов от 1 до 10 и встречается 5