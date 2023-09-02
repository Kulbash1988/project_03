# Оператор цикла  for перебираем элементы в коллекции
# применение Break (остонавливается при достижении цели), continue (пропускает части ниже себя) 

room_prices = [41, 94, 100, 7, 21, 92, 62, 49, 37, 17, ]
for price in room_prices:
    if price == max(room_prices):
        continue
    if price == min(room_prices):
       print('Минимальная цена:', price)
       break
    print('Текущая цена:', price)
print('До свидания!')

# использование pass (пропускает значение)
x = 4
if x > 0:
    pass
elif x < 0:
    pass
else:
    pass



# Задача 2
# Напишите код, который принимает список из чисел и возвращает сумму только положительных чисел в нем.

# Например
# [1,-4,7,12] -> 1 + 7 + 12 = 20

# Примечание:
# если положительных чисел в списке нет, то сумма равна 0.

primes = [1, -4, 7, 12]

# Вариант 1 с while

i = 0 
total = 0
while i < len(primes):
    if primes[i] >= 0:
        total += primes[i]
    i += 1    

print(total)


# # Вариант 2 с for

total = 0
for elem in primes: 
    if elem >= 0:
        total += elem

print(total)       


# Вариант 3 индексы for
# Генерация последовательности чисел
print(list(range(1000, 9999)))

total = 0
for ind in range(len(primes)):
    if primes[ind] >= 0:
        total += primes[ind]

print(total)        

# Вариант 4 функция enumerate()

total = 0
for ind, elem in enumerate(primes):
    print("Позиция элемента:", ind, "Элемент:", elem)
    if elem >= 0:
        total += elem

print(total)   

# Вариант 5 списковое включение
print(sum([x for x in primes if x > 0]))



