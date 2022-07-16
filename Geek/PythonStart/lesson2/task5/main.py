"""
Реализуйте алгоритм перемешивания списка.
"""
from random import randint, shuffle, sample


def make_list_num_n_elem(n):
    """
    Функция создает список из n - случайных элементов промежутка [-N, N].
    """
    listNum = []
    for i in range(n):
        listNum.append(randint(-1 * n, n))
    return listNum


def shuffle_list(list_el):
    """
    Функция перемешивает список.
    """
    newlist = []
    countlist = []
    while len(countlist) != len(list_el):
        pos = randint(0, len(list_el) - 1)
        if pos not in countlist:
            countlist.append(pos)
            newlist.append(list_el[pos])
    return newlist


list1 = make_list_num_n_elem(10)

list2 = list1.copy()
shuffle(list2)

print(list1)
print(list2)

list3 = shuffle_list(list1)
print(list3)