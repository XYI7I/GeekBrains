"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
"""
coorX1, coorY1 = int(input('координатa x первой точки x1: ')), int(input('координатa y первой точки y1: '))
coorX2, coorY2 = int(input('координатa x второй точки x2: ')), int(input('координатa y второй точки y2: '))

lenght_1_2 = (coorX2 - coorX1) ** 2 + (coorY2 - coorY1) ** 2
print('расстояние между ними в 2D пространстве - ', lenght_1_2 ** 0.5)