// See https://aka.ms/new-console-template for more information
Console.WriteLine("14. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно одновременно 7 и 23.");

Console.Write("Введите число: ");
int num1 = int.Parse(Console.ReadLine ());

if (num1 % 7 == 0 && num1 % 23 == 0)
{
    Console.WriteLine(num1 + " -> да");
}
else
{
    Console.WriteLine(num1 + " -> нет");
}
