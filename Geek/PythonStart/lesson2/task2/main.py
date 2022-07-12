"""
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""

def listFactN():
    N = int(input('Input N: '))
    listFactN = []
    for i in range(N):
        listFactN.append(findFact(i + 1))

    print(listFactN)

def findFact(n):
    """Поиск факториала"""
    facn = 1
    for i in range(1, n):
        facn = facn * i

    return facn

listFactN()
