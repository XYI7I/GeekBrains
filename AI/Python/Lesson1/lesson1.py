# coding: utf-8

# Основы языка Python.
# Занятие 1. Знакомство с Python

import time

print("Урок 1. Задание 1. Часть 1.")
numeric = 10
str = "Привет!"
print(numeric)
print(str)
print('***')

print("Урок 1. Задание 1. Часть 2.")
t = input("Введите время в секундах: ")
t = int(t)
time_string = time.strftime('%H:%M:%S', time.gmtime(t))
print(time_string)
print('***')

print("Урок 1. Задание 1. Часть 3.")
n = input("Введите число n: ")
sum = int(n) + int(n+n) + int(n+n+n)
print(sum)
print('***')

print("Урок 1. Задание 1. Часть 4.")
n = input("Введите введите целое положительное число : ")
a = []
i = 0
while i < len(n):
    a = a + [int(n[i])]
    i = i + 1
print('Самая большая цифра в числе: ', max(a))
print('***')

print("Урок 1. Задание 1. Часть 5.")
proceeds = int(input("Введите сумму выручки фирмы: "))
costs = int(input("Введите сумму издержек фирмы: "))
profit = proceeds - costs
if proceeds >= costs:
    print('Прибыль - выручка больше издержек на : ', profit, '$')
    print('Рентабельность фирмы : ', profit / proceeds)
    staff = int(input("Введите количество сотрудников фирмы: "))
    print('Прибыль фирмы в расчете на каждого сотрудника: ', profit / staff, '$')
else:
    print('Убыток - издержки больше выручки на : ', abs(profit), '$')
print('***')

print("Урок 1. Задание 1. Часть 6.")
a = int(input("Введите, результат спортсмена в первый день пробежки, км: "))
b = int(input("Введите, результат который должен достичь спортсмен, км: "))
if a >= b:
    while a >= b:
        print('Результат должен быть лучше(больше), чем в первый день!')
        b = int(input("Введите, результат который должен достичь спортсмен, км: "))
i = 1
while a < b:
    a = a * 1.1
    i = i +1
print(i)
print('На ', i,'-й день спортсмен достиг результата - не менее ', b, ' км.')

print('Задание выполнено!')
