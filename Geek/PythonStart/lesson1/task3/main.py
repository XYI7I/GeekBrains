"""
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
"""
coorX = 0
coorY = 0

while coorX ==0  or coorY == 0:
    coorX = int(input('Введите координату X (X ≠ 0): '))
    coorY = int(input('Введите координату Y (Y ≠ 0): '))

if coorX > 0:
    if coorY > 0:
        print('1')
    else:
        print('4')
else:
    if coorY > 0:
        print('2')
    else:
        print('3')