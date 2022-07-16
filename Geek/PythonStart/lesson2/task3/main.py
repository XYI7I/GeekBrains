"""
Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

Пример:

- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
"""


def make_list_subseq(n):
    """
    Функция создает список из n чисел последовательности (1+1/n)^n
    """
    listNum = []
    sum_el = 0
    for i in range(1, n + 1):
        num = (1 + 1 / i) ** i
        sum_el += num
        listNum.append(round(num, 4))
    return listNum, sum_el


listSubseq, SubseqSum = make_list_subseq(3)
print(f'Сумма элементов последовательности {listSubseq} = {round(SubseqSum, 4)}')