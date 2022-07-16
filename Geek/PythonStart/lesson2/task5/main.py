"""
Реализуйте алгоритм перемешивания списка.
"""
from random import randint, shuffle, sample


def make_list_num_n_elem(n):
    """
    Функция создает список из n - случайных элементов промежутка [-N, N].
    """
    list_num = []
    for i in range(n):
        list_num.append(randint(-1 * n, n))
    return list_num


def shuffle_list(list_el):
    """
    Функция перемешивает список.
    """
    new_list = []
    count_list = []
    while len(count_list) != len(list_el):
        pos = randint(0, len(list_el) - 1)
        if pos not in count_list:
            count_list.append(pos)
            new_list.append(list_el[pos])
    return new_list


list1 = make_list_num_n_elem(10)

list2 = list1.copy()
shuffle(list2)

print(list1)
print(list2)

list3 = shuffle_list(list1)
print(list3)
