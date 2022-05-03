# coding: utf-8

# Основы языка Python.
# Занятие 3. Знакомство с Python

# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
print("Урок 3. Задание 1.")

def div():
    quo = int(input('Введите число которое надо разделить: '))
    divider = int(input('Введите число на которое надо разделить: '))
    while divider == 0:
        print('Деление на 0 не возмлжно')
        divider = int(input('Введите число на которое надо разделить: '))
    ans = quo / divider
    return ans

ans = div()
print(ans)

print('***')

# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
print("Урок 3. Задание 2.")

def personal_data():
    name = input('Введите Имя: ')
    lastname = input('Введите Фамилию: ')
    year = input('Введите год рождения: ')
    city = input('Введите город проживания: ')
    email = input('Введите e-mail: ')
    phone = input('Введите телефон: ')
    print(name.title(), lastname.title(), year, city.title(), email, phone)

personal_data()

print('***')

# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
print("Урок 3. Задание 3.")

import numpy as np
def summ():
    a = []
    a = a + [int(input('Введите число: '))]
    a = a + [int(input('Введите число: '))]
    a = a + [int(input('Введите число: '))]
    Summa = np.sum(a) - min(a)
    print(Summa)
    return a
summ()

print('***')

# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
print("Урок 3. Задание 4.")

import math

def my_func(x, y):
    print(x**y)
    i = 0
    result = 1
    while i < math.fabs(y):
        result = result / x
        i += 1
    print(result)

arg1 = int(input('Введите целое положительное число x: '))
while arg1 < 0:
    print('Число должно быть положительным')
    arg1 = int(input('Введите целое положительное число x: '))

arg2 = int(input('Введите целое отрицательное число y: '))
while arg2 > 0:
    print('Число должно быть отрицательным')
    arg2 = int(input('Введите целое отрицательное число y: '))

my_func(arg1, arg2)

print('***')

# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
print("Урок 3. Задание 5.")

def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input(' Введите строку чисел, разделенных пробелом. При нажатии Enter выводится сумма чисел. Q - для выхода ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма: {sum_res}')
    print(f'Итоговая сумма всех чисел: {sum_res}')


my_sum()

print('***')

# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
print("Урок 3. Задание 6.")

def func_title(wordlat):
    wordlat = wordlat.title()
    return wordlat

print(func_title(input('Введите слово: ')))

input_str = input("Введите строку из нескольких слов, разделённых пробелами: ")
s = ""
a = input_str.split()
for el in range(len(a)):
    s = func_title(s + a[el] + ' ')
print(s)

print('Задание выполнено!')