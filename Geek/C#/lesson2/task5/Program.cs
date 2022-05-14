// 16. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
Console.WriteLine("Программа, принимает на вход два числа и проверяет, является ли одно число квадратом другого.");

Console.Write("Первое число: ");
int num1 = int.Parse(Console.ReadLine ());

Console.Write("Второе число: ");
int num2 = int.Parse(Console.ReadLine ());

string res =  num1 == num2 * num2 || num2 == num1 * num1 ? $"{num1}, {num2} -> да" : $"{num1}, {num2} -> нет";
Console.WriteLine(res);
