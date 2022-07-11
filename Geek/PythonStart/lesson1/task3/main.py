"""
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
"""

def findQuarter(x, y):
    if x > 0 and y > 0:
        numQ = 1
    elif x < 0 and y > 0:
        numQ = 2
    elif x < 0 and y < 0:
        numQ = 3
    else:
        numQ = 4

    print(f"Точка находится в {numQ} - четверти плоскости")

coorX = 0
coorY = 0

while coorX == 0 or coorY == 0:
    coorX = int(input('Введите координату X (X ≠ 0): '))
    coorY = int(input('Введите координату Y (Y ≠ 0): '))

findQuarter(coorX, coorY)
