"""
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""

list_float_el = [1.1, 1.2, 3.1, 5, 10.01]


def find_sub_max_min_frac_part(list_num):
    """
    Функция находит разницу между максимальным и минимальным значением дробной части элементов

    Пример:
    - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
    """
    min_frac = 1
    max_frac = 0

    for el in list_num:
        if el % 1 > max_frac:
            max_frac = el % 1
        if el % 1 < min_frac and el % 1 != 0:
            min_frac = el % 1
            n = len(str(el)) - str(el).index('.') - 1

    sub_frac_el = round(max_frac - min_frac, n)
    return sub_frac_el


find_sub = find_sub_max_min_frac_part(list_float_el)

print(f'Разница между максимальным и минимальным значением дробной части элементов списка {list_float_el} = {find_sub}')
