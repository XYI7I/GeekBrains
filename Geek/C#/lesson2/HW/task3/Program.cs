// Задача 13: Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.
Console.WriteLine("Программа, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.");

Console.Write("Введите число: ");

int num = int.Parse(Console.ReadLine());

int absnum = Math.Abs(num);
string text = absnum.ToString();
string res = text.Length < 3 ? $"{num} - третьей цифры нет" : $"{num} -> {text[2]}";

Console.WriteLine(res);