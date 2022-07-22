"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
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
