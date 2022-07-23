"""
Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
"""
import math


def find_pi_acc(acc_range):
    """
    Функция находит число π c заданной точностью d

    Пример: при d = 0.001, π = 3.141    10^{-10} ≤ d ≤ 10^{-1}
    """
    pi = 3
    count = 1
    while round(pi, acc_range + 1) != round(math.pi, acc_range + 1):
        pi += (-1)**(count + 1) * 4 / (2 * count * (2 * count + 1) * (2 * count + 2))
        count += 1

    return round(pi, acc_range)


acc_range = 10
find_pi = find_pi_acc(acc_range)
print(f'Число π c заданной точностью {acc_range} = {find_pi}')
print(f'Число π = {round(math.pi, acc_range)}')