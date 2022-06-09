#Для перевозки партии грузов различной массы выделен грузовик, но его грузоподъёмность ограничена, поэтому перевезти
# сразу все грузы не удастся. Грузы массой от 180 до 200 кг грузят в первую очередь, выбирая грузы по убыванию массы,
# начиная с самого тяжёлого. На оставшееся после этого место стараются взять как можно большее количество грузов.
# Если это можно сделать несколькими способами, выбирают тот способ, при котором самый большой из выбранных грузов имеет
# наибольшую массу. Если и при этом условии возможно несколько вариантов, выбирается тот, при котором наибольшую массу
# имеет второй по величине груз, и т.д. Известны количество грузов, масса каждого из них и грузоподъёмность грузовика.
# Необходимо определить количество и общую массу грузов, которые будут вывезены при погрузке по вышеописанным правилам.

base_weights = [] # список масс [180; 200]
add_weights = [] # список остальных масс

with open('26.txt') as inp:
    n, m = map(int, inp.readline().split())
    for _ in range(n):
        weight = int(inp.readline())
        if 180 <= weight <= 200:
            base_weights.append(weight)
        else:
            add_weights.append(weight)

add_weights.sort()
# sum_weights - итоговая сумма масс
sum_weights = sum(base_weights)
# если m < sum_weights, то даже группы массами [180; 200] не все влезут
# массы, учтенные в sum_weights, назовем массами погруженных товаров
m -= sum_weights
# определим максимальное количество товаров, которые можно погрузить
# для этого пройдемся по ещё не  погреженным товарам
# и будем "грузить" их пока они не вмещаются по массе
i = 0
while m >= add_weights[i]:
    m -= add_weights[i]
    sum_weights += add_weights[i]
    i += 1

print('Количество грузов', len(base_weights) + i)
#сейчас погружено максимально возможное количество грузов минимальной массы попробуем заменить их более тяжелыми грузами
k = len(add_weights) - 1
changes = 0 # количество замен
for j in range(i - 1, -1, -1):
    m += add_weights[j]
    while m < add_weights[k]:
        k -= 1
    # changes позволяет нам погрузить обратно грузы, которые были заменены на более тяжелые
    if k < i - changes:
        break
    m -= add_weights[k] # грузим
    # в общей массе заменяем легкий товар более тяжелым:
    sum_weights = sum_weights - add_weights[j] + add_weights[k]
    changes += 1
    k -= 1

print('Общая масса груза', sum_weights)