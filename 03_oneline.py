# Что можно получить из словаря?
# print(employees.keys())
# print(employees.values())
# print(employees.items())
# print(tuple(employees)) значение не будет


# Вспомним
# lst = [1, 2, 3] изменяемый обьект
# tpl = (1, 2, 3) неизменяемый обьект
# str = "Hello" неизменяемые
# set = set((1, 2, 3)) изменяемые

# словарь изменяемый обьект, который состоит из ключа и значение (типо мяч - синий, апельсин - оранжевый)
# dct = {}
# получить значение из словаря
# print(capitals["Италия"])
# добавить значение в словарь
# capitals["Франция"] = "Париж"
# print(capitals)


# Задача 3 Поиск самых высокооплачеваемых работников
# нужно найти всех сотрудников, зарабатывающих по крайней мере 100 000 долларов  в год

# Вариант 1

employees = {
    "Alis" : 100000,
    "Bob" : 99817,
    "Carol" : 122908,
    "Frank" : 88123,
    "Eve" : 93121
}

top_mgrs = []
for name in employees.keys():
    if employees[name] >= 100000:
        top_mgrs.append(name)

print(top_mgrs) 

#  ['Alis', 'Carol']

# Вариант 2 списковые включения (однострочники) цикл записан в одну строку
# # Пояснение к варианту 2 с примерами:
                           # x = 4
                           # if x > 0:
                           #     print("больше 0")
                           # else:
                           #     print("Меньше 0")    

                           # # Можно записать в одну строку
                           # print("Больше 0" if x > 0 else "Меньше 0")    

                           # # Или можем использовать for
                           # for i in [1, 2, 3]:
                           #     print(i**2)
                           # # или одной строкой
                           # print([i**2 for i in [1, 2, 3]])    
# # Решение 1
top_mgrs = [employees[n] >= 100000 for n in employees]
print(top_mgrs)
# [True, False, True, False, False]

# Решение 2
top_mgrs = [n for n in employees if employees[n] >= 100000]
print(top_mgrs)
# ['Alis', 'Carol']

# Решение 3
top_mgrs = [n for n, s in employees.items() if s >= 100000]
print(top_mgrs)
# ['Alis', 'Carol']




