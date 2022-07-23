"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
<<<<<<< HEAD

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


print(f'Число π c заданной точностью {acc_range} = {find_pi}')
=======
"""
import math


def find_simp_div_n(n):
    """
    Функция составит список простых множителей числа

    """
    pi = 3
    count = 1
    while round(pi, acc_range + 1) != round(math.pi, acc_range + 1):
        pi += (-1)**(count + 1) * 4 / (2 * count * (2 * count + 1) * (2 * count + 2))
        count += 1

    return round(pi, acc_range)


def find_simp_num_n(n):
    """
    Функция находит все простые числа в интервале от 1 до n.
    """
    file = open('simpl_num.txt', 'w')
    for i =

    Lines = file.readlines()
    mult = 1
    for line in Lines:
        mult *= list_n[int(line)]
    return mult


list1 = make_list_num_n_elem(10)
print(list1)

mult_list_el = find_mult_list_el_position(list1)
print(f'произведение элементов на указанных позициях (file.txt) = {mult_list_el}')

acc_range = 10
find_pi = find_pi_acc(acc_range)
print(f'Число π c заданной точностью {acc_range} = {find_pi}')
print(f'Число π = {round(math.pi, acc_range)}')
>>>>>>> 9f310d94b1d48039ce14b33b0ededa1f217d8ca1
