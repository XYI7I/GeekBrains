// 22. Напишите программу, которая принимает на вход число (N) и выдаёт таблицу квадратов чисел от 1 до N.
Console.WriteLine("Программа, принимает на вход число (N) и выдаёт таблицу квадратов чисел от 1 до N.");

Console.Write("Ведите число N: ");
int Num = int.Parse(Console.ReadLine ());

int[] arr = new int[Num];

for (int i = 0; i < Num; i++)
{
    arr [i] = (i + 1) * (i + 1);
}

var str = string.Join(" ", arr);
Console.WriteLine($"{Num} -> {str}");



void SquareArray(int Num)
{
    int[] array = new int[Num];
    for (int i = 0; i < Num; i++)
    {
        array [i] = (i + 1) * (i + 1);
    }
    var str = string.Join(" ", array);
    Console.WriteLine($"{Num} -> {str}");
}

SquareArray(Num);