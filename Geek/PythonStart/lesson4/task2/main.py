"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

"""


def find_list_simpl_div(n):
    """
    Функция находит число π c заданной точностью d

    Пример: при d = 0.001, π = 3.141    10^{-10} ≤ d ≤ 10^{-1}
    """
    pi = 3
    i = 1
    while round(pi, acc_range + 1) != round(math.pi, acc_range + 1):
        pi += (-1)**(i + 1) * 4 / ( 2 * i * (2 * i + 1) * (2 * i + 2))
        i += 1

    return round(pi, acc_range)

def find_simpl_num(num):
    """
    Определение простое число или нет
    """
    for i in range(2, abs(num)):
        if num % i == 0:
            print(f'Число {num} - не простое')
            return
    print(f'Число {num} - простое')