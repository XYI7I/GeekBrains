"""
Напишите программу:

- найти факториал числа

- проверить число на простоту (т.е. что число делится только на 1 и само на себя)

- найти наибольший простой делитель числа
"""


def findFact():
    """Поиск факториала"""
    n = -1
    while n < 0:
        n = int(input('введите n (n ≥ 0): '))
    facn = 1

    for i in range(1, n):
        facn = facn * 1

    print(f'Факториал числа {n} - {n}! = {facn}')

def findSimplNum():
    """Определение простое число или нет"""
    num = int(input('введите число: '))
    for i in range(2, num):
        if num % i == 0:
            print(f'Число {num} - не простое')
            return
    print(f'Число {num} - простое')

def findLargDiv():
    """Определение простое число или нет"""
    num = int(input('введите число: '))
    maxdiv = 1
    for i in range(2, num):
        if num % i == 0:
            maxdiv = i

    print(f'Наибольший делитель числа {num} = {maxdiv}')

findFact()
findSimplNum()
findLargDiv()
