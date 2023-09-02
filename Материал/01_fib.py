# Задача 1: Последовательность Фибоначчи

# Чему равен 100 элемент?
# 1 2 3 4 5 6
# 1 1 2 3 4 7


fib1, fib2 = 1, 1
n = input("Номер элемента ряда Фибоначчи: ")

# Вариант 1 через while

i = int(n) - 2

while i > 0:
    print(fib2)
    fib1, fib2 = fib2, fib1 + fib2
    i -= 1

print("Значение этого элемента:", fib2)

# Вариант 2 через for

for i in range(2, int(n)):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2)