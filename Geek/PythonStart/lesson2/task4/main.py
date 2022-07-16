"""
 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
 """
from random import randint


def make_list_num_n_elem(N):
    """
    Функция создает список из n - случайных элементов промежутка [-N, N].
    """
    listNum = []
    for i in range(N):
        listNum.append(randint(-1 * N, N))
    return listNum


def find_mult_list_el_position(list_n):
    """
    Функция находит произведение элементов списка находящихся на позициях заданых в текстовом файле.
    """
    file = open('file.txt', 'r')
    Lines = file.readlines()
    mult = 1
    for line in Lines:
        mult *= list_n[int(line)]
    return mult


list1 = make_list_num_n_elem(10)
print(list1)

mult_list_el = find_mult_list_el_position(list1)
print(f'произведение элементов на указанных позициях (file.txt) = {mult_list_el}')