nado = 1 #что должны получить 0 или 1 для таблицы
for x in range(0, 2):
	for y in range(0, 2):
		for z in range(0, 2):
			for w in range(0, 2):
				if((not(y) or w) == (not(x) or not(z)) and (x or w)) == nado: #в скобках пишем уравнение
					print(x, y, z, w)