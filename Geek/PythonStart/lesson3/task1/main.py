"""
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

"""

list_num = [2, 3, 5, 9, 3]


def find_sum_el_odd_pos(list_num):
    """
    Функция находит сумму элементов на нечетных позициях

    :param list_num: - список из чисел
    """
    sum_el = 0
    for i in range(1, len(list_num), 2):
        sum_el += list_num[i]
    return sum_el


find_sum = find_sum_el_odd_pos(list_num)
print(find_sum)
