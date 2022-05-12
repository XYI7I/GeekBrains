// See https://aka.ms/new-console-template for more information
Console.WriteLine("11. Напишите программу, которая выводит случайное трёхзначное число и удаляет вторую цифру этого числа.");

Random rnd = new Random();
int num = rnd.Next(100, 1000);

Console.WriteLine("Число = " + num);

string text = num.ToString();

Console.WriteLine("Модификация трехзначного числа: " + num + " -> " + text[0] + text[2]);