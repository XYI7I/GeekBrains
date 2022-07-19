"""
Вычислить число π c заданной точностью d

Пример:
при d = 0.001, π = 3.141    10^{-10} ≤ d ≤ 10^{-1}

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
print(f' Сумма элементов на нечётных позициях списка {list_num} = {find_sum}')
