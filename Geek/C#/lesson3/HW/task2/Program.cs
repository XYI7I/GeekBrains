// 21. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.
Console.WriteLine("Программа, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.");

// Координаты первой точки
Console.Write("Ведите координату первой точки X1: ");
int coord_X1 = int.Parse(Console.ReadLine ());
Console.Write("Ведите координату первой точки Y1: ");
int coord_Y1 = int.Parse(Console.ReadLine ());
Console.Write("Ведите координату первой точки Z1: ");
int coord_Z1 = int.Parse(Console.ReadLine ());

// Координаты второй точки
Console.Write("Ведите координату второй точки X2: ");
int coord_X2 = int.Parse(Console.ReadLine ());
Console.Write("Ведите координату второй точки Y2: ");
int coord_Y2 = int.Parse(Console.ReadLine ());
Console.Write("Ведите координату первой точки Z2: ");
int coord_Z2 = int.Parse(Console.ReadLine ());

void Distance(int x1, int y1, int z1, int x2, int y2, int z2)
{
    int x = x2 - x1;
    int y = y2 - y1;
    int z = z2 - z1;
    double dis = Math.Sqrt(x * x + y * y + z * z);
    Console.WriteLine($"A({x1}, {y1}, {z1}); B({x2}, {y2}, {z2}) -> {Math.Round(dis, 2)}");
}

Distance(coord_X1, coord_Y1, coord_Z1, coord_X2, coord_Y2, coord_Z2);