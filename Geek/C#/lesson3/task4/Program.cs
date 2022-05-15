// 21. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Console.WriteLine("Программа, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.");

Console.Write("Ведите координату первой точки X1: ");
int coord_X1 = int.Parse(Console.ReadLine ());
Console.Write("Ведите координату первой точки Y1: ");
int coord_Y1 = int.Parse(Console.ReadLine ());

Console.Write("Ведите координату второй точки X2: ");
int coord_X2 = int.Parse(Console.ReadLine ());
Console.Write("Ведите координату второй точки Y2: ");
int coord_Y2 = int.Parse(Console.ReadLine ());

double R_AB = Math.Sqrt((coord_X2 - coord_X1) * (coord_X2 - coord_X1) + (coord_Y2 - coord_Y1) * (coord_Y2 - coord_Y1));

Console.WriteLine($"A({coord_X1}, {coord_Y1}); B({coord_X2}, {coord_Y2}) -> {R_AB}");