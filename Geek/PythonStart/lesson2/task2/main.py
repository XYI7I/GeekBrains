"""
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""


def list_fact_n():
    """
    Создаем список факториала
    """
    N = int(input('Input N: '))
    listFactN = []
    for i in range(N):
        listFactN.append(find_fact(i + 1))

    print(listFactN)


def find_fact(n):
    """
    Поиск факториала
    """
    fac_n = 1
    for i in range(1, n):
        fac_n = fac_n * (i + 1)

    return fac_n


list_fact_n()
