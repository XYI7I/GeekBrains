"""
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

"""
def make_list_num_n_elem(N):
    """
    Функция создает список из n - случайных элементов промежутка [-N, N].
    """
    listNum = []
    for i in range(N):
        listNum.append(randint(-1 * N, N))
    return listNum


def make_not_rep_list(list):
    """
    Функция которая выведет список неповторяющихся элементов исходной последовательности.
    """

    for elem in list:
        if list.count(elem) > 1:
            list.remove(elem)

    print(list)

    return

A = [10, 10, 23, 10, 123, 66, 78, 123]

make_not_rep_list(A)