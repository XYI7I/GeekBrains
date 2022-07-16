"""
Задайте список. Напишите программу, которая определит присутсвует ли в заданном списке строк некое число.

"""

list_str = ['asd1', '23', 'asd', '87']
find_num = '12'

for el in list_str:
    if el.find(find_num) > 0:
        print('yes')
        break