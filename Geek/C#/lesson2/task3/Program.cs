﻿// 12. Напишите программу, которая будет принимать на вход два числа и выводить, является ли первое число кратным второму. Если число 2 не кратно числу 1, то программа выводит остаток от деления.
Console.WriteLine("Программа, принимает на вход два числа и выводит, является ли первое число кратным второму. Если число 2 не кратно числу 1, то программа выводит остаток от деления.");

Console.Write("Первое число: ");
int num1 = int.Parse(Console.ReadLine ());

Console.Write("Второе число: ");
int num2 = int.Parse(Console.ReadLine ());

string res =  num1 % num2 == 0 ? $"{num1}, {num2} -> кратно" : $"{num1}, {num2} -> не кратно, остаток {num1 % num2}";

Console.WriteLine(res);