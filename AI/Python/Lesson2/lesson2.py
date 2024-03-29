# coding: utf-8

# Основы языка Python.
# Занятие 1. Знакомство с Python

# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

print("Урок 2. Задание 1.")

my_list = [13, 'Hi', 269, 1.3, None, 'Excellent']


def my_type(elements):
    for elements in range(len(my_list)):
        print(type(my_list[elements]))
    return


my_type(my_list)
print(my_list)

print('***')

# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

print("Урок 2. Задание 2.")

el_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
el = 0

while i < el_count:
    my_list.append(input("Введите следующее значение списка "))
    i += 1
for elem in range(int(len(my_list) / 2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2

print(my_list)
print('***')

# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

print("Урок 2. Задание 3.")
n = int(input("Введите число от 1 до 12: "))
seas_list = ['Зима', 'Весна', 'Лето', 'Осень']
seas_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}

if n == 1 or n == 12 or n == 2:
    print(seas_dict.get(1))
    print(seas_list[0])
elif n == 3 or n == 4 or n == 5:
    print(seas_dict.get(2))
    print(seas_list[1])
elif n == 6 or n == 7 or n == 8:
    print(seas_dict.get(3))
    print(seas_list[2])

elif n == 9 or n == 10 or n == 11:
    print(seas_dict.get(4))
    print(seas_list[3])
else:
    print("Такого месяца не существует")

print('***')

# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
# необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

print("Урок 2. Задание 4.")

input_str = input("Введите строку из нескольких слов, разделённых пробелами: ")

num = 1
lessSpace = input_str.split()

for index, el in enumerate(lessSpace):
    # print(f" {num} {el[0:10]}")
    print(f" {index + 1} {el[0:10]}")
    num += 1

print('***')

# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

print("Урок 2. Задание 5.")
my_list = [7, 5, 3, 3, 2]
digit = int(input("Введите число от 0 до 9: "))

my_list.append(digit)
my_list.sort(reverse=True)

print(f"текущий список - {my_list}")
print('***')

# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (
# характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
print("Урок 2. Задание 6.")

index = 1
result = []

specification = ['название', 'цена', 'количество', 'eд']

while True:
    question = input("Add new item? (Yes/No)")

    if question.lower() != 'yes' and question.lower() != 'y':
        break

    item = {}

    for spec in specification:
        item_data = input(f"Input {spec}: ")

        if item_data.isdigit():
            item[spec] = int(item_data)
        else:
            item[spec] = item_data

    result.append(tuple([index, item]))

    index += 1

print(result)

result_dict = {}

for item in specification:

    for _, param in result:

        if result_dict.get(item):
            result_dict[item].append(param.get(item))
        else:
            result_dict[item] = [param.get(item)]

print(result_dict)

print('Задание выполнено!')
