# coding: utf-8

# Основы языка Python.
# Занятие 2. Знакомство с Python

# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
print("Урок 2. Задание 1.")
my_list = [13, 'Hi', 269, 1.3, None,'Excellent']
for el in range(len(my_list)):
    print(type(my_list[el]))
    el += 1
print(my_list)
print('***')

# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
print("Урок 2. Задание 2.")
el_count = int(input("Введите количество элементов в списке "))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("Введите элемент списка: "))
    i += 1
for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)
print('***')

# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
print("Урок 2. Задание 3.")
n = int(input("Введите число от 1 до 12: "))
seas_list = ['Зима', 'Весна', 'Лето', 'Осень']
seas_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
if n ==1 or n == 12 or n == 2:
        print(seas_dict.get(1))
        print(seas_list[0])
elif n == 3 or n == 4 or n ==5:
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

# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
print("Урок 2. Задание 4.")
input_str = input("Введите строку из нескольких слов, разделённых пробелами: ")
a = input_str.split()
for el in range(len(a)):
    if len(a[el]) <= 10:
        print(a[el])
    else:
        print(a[el][0:10])
print('***')

# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
print("Урок 2. Задание 5.")
my_list = [7, 5, 3, 3, 2]
digit = int(input("Введите число от 0 до 9: "))
for el in range(len(my_list)):
    if my_list[el] == digit:
        my_list.insert(el + 1, digit)
        break
    elif my_list[0] < digit:\
            my_list.insert(0, digit)
    elif my_list[-1] > digit:\
            my_list.append(digit)
    elif my_list[el] > digit and my_list[el + 1] < digit:\
            my_list.insert(el + 1, digit)
print(f"текущий список - {my_list}")
print('***')

# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
print("Урок 2. Задание 6.")
# my_item = [
#     (1, {'название' : 'компьютер', 'цена' : 20000, 'количество' : 5, 'eд' : 'шт.'}),
#     (2, {'название' : 'принтер', 'цена' : 6000, 'количество' : 2, 'eд' : 'шт.'}),
#     (3, {'название' : 'сканер', 'цена' : 2000, 'количество' : 7, 'eд' : 'шт.'})
# ]
# print(my_item)
# print(my_item.keys('название'))
products, order = [], 1
title, price, amount = None, None, None

while True:
    if title is None:
        tmp = input('Введите название товара: ')
        if not tmp.isalnum():
            print('Наименование товара не может быть пустым. Попробуйте еще раз.')
            continue

        title = tmp

    if price is None:
        tmp = input('Введите стоимость товара: ')
        if not tmp.isdigit():
            print('Цена должна быть целым числомю. Попробуйте еще раз.')
            continue

        price = int(tmp)

    if amount is None:
        tmp = input('Введите количество: ')
        if not tmp.isdigit():
            print('Количество должно быть целым числом. Попробуйте еще раз.')
            continue

        amount = int(tmp)

    tmp = input('Введите единицы измерения: ')
    if not tmp.isalpha():
        print('Единица изменерения не может быть пустой. Попробуйте еще раз.')
        continue

    unit = tmp

    products.append((
        order,
        {
            'Наименование': title,
            'Цена': price,
            'Количество': amount,
            'Единица': unit
        }
    ))

    title, price, amount = None, None, None
    order += 1

    print(products)

    q = input('Формирование списка завершено? (Y/N)) ')
    if q.lower() == 'y':
        break

analitics = {
    'Наименование': [],
    'Цена': [],
    'Количество': [],
    'Единица': set()
}

for _, item in products:
    analitics['Наименование'].append(item['Наименование'])
    analitics['Цена'].append(item['Цена'])
    analitics['Количество'].append(item['Количество'])
    analitics['Единица'].add(item['Единица'])

print(analitics)

print('Задание выполнено!')
