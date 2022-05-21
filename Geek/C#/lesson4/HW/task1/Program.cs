// Задача 25: Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.
Console.WriteLine("Программа принимает на вход два числа (A и B) и возводит число A в натуральную степень B.");

void PowNum(int a, int b)
{
    int pownum = a;
    for (int i = 1; i < b; i++)
    {
         pownum = pownum * pownum;
    }

    Console.WriteLine($"{a} в степени {b} = {pownum}");
}

Console.Write("Введите число: ");
int num = int.Parse(Console.ReadLine ());

Console.Write("Введите в какую степень возвести число: ");
int pow = int.Parse(Console.ReadLine ());

PowNum(num, pow);