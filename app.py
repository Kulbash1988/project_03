################################################################  Импорт  ##############################################################################
# Модуль app.py - стартовый запуск скрипта
###########################################################  Терминалогияn  ############################################################################
# Модуль - файл, в котором мы работаем. Модуль рассматривается как отдельный обьект в Python. Содержит в себе набор имен (имена переменных, функций и т.д.)
# Пакет - папка с модулями, которая содержит фаил __init__
# Библиотека - набор пакетов и модулей, например Python Standart Library
# Фреймворк

########################################################################################################################################################
#                                                               Импорт имен
########################################################################################################################################################

# # Вариант №1 - просто импорт модуля

# import functions
# # functions - имя импортируемого файла
# print(functions.sum_all(100, 20, 300))

# # Вариатн №2 - импорт с синонимом

# import functions as f

# print(f.sum_all(100, 20, 300))

# # Вариан №3 - конкретного имени (Осторожно! может перекрыть имя) (Практический пример: from flas import Flask)

# from functions import sum_all

# print(sum_all(100, 20, 300))

# # Вриант №4 - перенос всех имен (пример в призентации)

# ##########################################################################################################################################################
# #                                                       Запуск скрипта по имини модуля
# ##########################################################################################################################################################

# if __name__ == "__main__":
#     print("Запуск скрипта")
#     print(f.get_topmgrs({'Sam': 100000, 'Paul':50000}))
#     print(sum_all(100, 20, 300))

# # __name__ это модуль __main__, который является исполняемым

# ###########################################################################################################################################################
# #                                                           Структура модуля
# ###########################################################################################################################################################

# # По порядку:
# # 1 Импорты (import os)
# # 2 Констаны (PATH='C:\User\...') - лучше без них
# # 3 функции (def func(par):)
# # 4 Классы (class Person:)
# # 5 Тело цикла - условия

# # перенменные в модуле лучше не обьявлять
# # переменные

# ###########################################################################################################################################################
# #                                                           Импорт из пакетов
# ###########################################################################################################################################################

# # 1 - просто импотр из пакета

# import my_package.module_2
# my_package.module_2.foo_2

# # 2 - импорт с синонимом
# # Практический пример: Import matplotinb.pyploy as pit 

# import my_package.module_2 as m2
# m2.foo_2

# # 3 - импорт напрямую из пакета

# import my_package.subpackage as sp
# sp.foo_3()

# ############################################################################################################################################################
# #                                                           Импорт встроеных пакетов
# ############################################################################################################################################################

import random #- генератор случайных событий
import time #- работа с временем
import os #- взвимодействия файла с файловой системой

# Пример
while True:
    print(random.randint(0, 100))
    time.sleep(3) # Ctrl+C чтобы остановитьъ

################################################################################################################################################################
#                                                             Импорт внешних пакетов
################################################################################################################################################################

# Предворительно их нужно установить
#Например командой pip install line-profiler (это имя модуля внутри файла написаный зеленым цветом)
    