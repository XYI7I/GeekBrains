// 40. Напишите программу, которая принимает на вход три числа и проверяет, может ли существовать треугольник с сторонами такой длины.
Console.WriteLine("Программа, принимает на вход три числа и проверяет, может ли существовать треугольник с сторонами такой длины.");

// Длины сторон треугольника
Console.Write("Ведите длину первой стороны L1: ");
int len1 = int.Parse(Console.ReadLine ());
Console.Write("Ведите длину первой стороны L2: ");
int len2 = int.Parse(Console.ReadLine ());
Console.Write("Ведите длину первой стороны L2: ");
int len3 = int.Parse(Console.ReadLine ());


void Treangle(int l1, int l2, int l3)
{
    if (l1 < l2 + l3 && l2 < l1 + l3 && l3 < l1 + l2 )
        Console.WriteLine("Yes");
    else
        Console.WriteLine("No");
}

Treangle(len1, len2, len3);