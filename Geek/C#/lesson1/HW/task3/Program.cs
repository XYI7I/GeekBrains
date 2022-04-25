// See https://aka.ms/new-console-template for more information
Console.WriteLine("Задача 3. Программа на вход принимает число и выдаёт, является ли число чётным.");

Console.Write("Введите число: ");
int numa = int.Parse(Console.ReadLine ());
// int test = numa % 2;
if (numa % 2 == 0)
{
    Console.WriteLine("число чётноё");
}
else
{
    Console.WriteLine("число нечётноё");
}