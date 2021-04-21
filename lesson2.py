# coding: utf-8

# Библиотеки Python для Data Science: Numpy, Matplotlib, Scikit-learn.
# Занятие 2. Работа с данными в Pandas
import numpy as np
import pandas as pd

''' Задание 1
Импортируйте библиотеку Pandas и дайте ей псевдоним pd. Создайте датафрейм authors со столбцами author_id и author_name, в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные:  
[1, 1, 1, 2, 2, 3, 3],
['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
[450, 300, 350, 500, 450, 370, 290].
'''
authors = pd.DataFrame({'author_id':[1, 2, 3], 'author_name':['Тургенев', 'Чехов', 'Островский']}, columns=['author_id', 'author_name'])
book = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3], 'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'], 'price':[450, 300, 350, 500, 450, 370, 290]}, columns=['author_id', 'book_title', 'price'])


print("Урок 2. Задание 1.")

part1 = input('Выполнить задание 1? (Y) ')
if part1.title() == 'Y':
    answer = ''
    while answer.title() != 'Y':
        print(authors)
        print(book)
        answer = input('Закончить выполнение задания 1? (Y) ')
else:
    pass
print('***')

authors_price = pd.merge(authors, book, on = 'author_id', how = 'outer')

''' Задание 2
Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.
'''

print("Урок 2. Задание 2.")

part1 = input('Выполнить задание 2? (Y) ')
if part1.title() == 'Y':
    answer = ''
    while answer.title() != 'Y':
        print(authors_price)
        answer = input('Закончить выполнение задания 2? (Y) ')
else:
    pass
print('***')

top5 = authors_price.nlargest(5, 'price')

''' Задание 3
Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.
'''

print("Урок 2. Задание 3.")

part1 = input('Выполнить задание 3? (Y) ')
if part1.title() == 'Y':

    answer = ''
    while answer.title() != 'Y':
        print(top5)
        answer = input('Закончить выполнение задания 3? (Y) ')
else:
    pass
print('***')

''' Задание 4
Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
author_name, min_price, max_price и mean_price, в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.
'''

print("Урок 2. Задание 4.")

part1 = input('Выполнить задание 4? (Y) ')
if part1.title() == 'Y':

    answer = ''
    while answer.title() != 'Y':
        authors_stat = authors_price['author_name'].value_counts()
        authors_stat = authors_price.groupby('author_name').agg({'price': ['min', 'max', 'mean']})
        print(authors_stat)
        authors_stat = authors_stat.rename(columns={'min': 'min_price', 'max': 'max_price', 'mean': 'mean_price'})
        print(authors_stat)
        answer = input('Закончить выполнение задания 4? (Y) ')
else:
    pass
print('***')

''' Задание 5**
Создайте новый столбец в датафрейме authors_price под названием cover, в нем будут располагаться данные о том, какая обложка у данной книги - твердая или мягкая. В этот столбец поместите данные из следующего списка:
['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая'].
Просмотрите документацию по функции pd.pivot_table с помощью вопросительного знака.Для каждого автора посчитайте суммарную стоимость книг в твердой и мягкой обложке. Используйте для этого функцию pd.pivot_table. При этом столбцы должны называться "твердая" и "мягкая", а индексами должны быть фамилии авторов. Пропущенные значения стоимостей заполните нулями, при необходимости загрузите библиотеку Numpy.
Назовите полученный датасет book_info и сохраните его в формат pickle под названием "book_info.pkl". Затем загрузите из этого файла датафрейм и назовите его book_info2. Удостоверьтесь, что датафреймы book_info и book_info2 идентичны.
'''

print("Урок 2. Задание 5.")

part1 = input('Выполнить задание 5? (Y) ')
if part1.title() == 'Y':

    answer = ''
    while answer.title() != 'Y':
        authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']
        print(authors_price)

        book_info = pd.pivot_table(authors_price, values='price', index=['author_name'], columns=['cover'], aggfunc=np.sum)
        book_info['мягкая'] = book_info['мягкая'].fillna(0)
        book_info['твердая'] = book_info['твердая'].fillna(0)
        print(book_info)

        answer = input('Закончить выполнение задания 5? (Y) ')
else:
    pass
print('Задание урока 2 выполнены!')