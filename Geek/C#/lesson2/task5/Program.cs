// 16. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
Console.WriteLine("Программа, принимает на вход два числа и проверяет, является ли одно число квадратом другого.");

Console.Write("Первое число: ");
int num1 = int.Parse(Console.ReadLine ());

Console.Write("Второе число: ");
int num2 = int.Parse(Console.ReadLine ());


if (num1 == Math.Pow(num2, 2) || num2 == Math.Pow(num1, 2))
{
    Console.WriteLine(num1 + ", " + num2 + " -> да");
}
else
{
    Console.WriteLine(num1 + ", " + num2 + " -> нет");
}