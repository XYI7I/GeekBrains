// 17. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
Console.WriteLine("Программа, принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.");

int coord_X = 0;
int coord_Y = 0;
string res = null;

while (coord_X == 0 || coord_Y == 0)
{
    Console.Write("Ведите координату X, (X ≠ 0): ");
    coord_X = int.Parse(Console.ReadLine ());
    
    Console.Write("Ведите координату Y, (Y ≠ 0): ");
    coord_Y = int.Parse(Console.ReadLine ());
}

if (coord_X > 0)
{
    res = coord_Y > 0 ? $"1" : $"4";

}
else
{
    res = coord_Y > 0 ? $"2" : $"3";
}

Console.WriteLine(res);