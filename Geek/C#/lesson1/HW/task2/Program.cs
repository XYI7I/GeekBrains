// See https://aka.ms/new-console-template for more information
Console.WriteLine("Задание 2. Программа принимает на вход три числа и выдаёт максимальное из этих чисел.");

Console.Write("Первое число: ");
int numa = int.Parse(Console.ReadLine ());

Console.Write("Второе число: ");
int numb = int.Parse(Console.ReadLine ());

Console.Write("Третье число: ");
int numc = int.Parse(Console.ReadLine ());

int maxnum = numa;

if (numb > maxnum)
{
    maxnum = numb;
}

if (numc > maxnum)
{
    maxnum = numc;
}

Console.WriteLine("Максимальное число: " + maxnum);