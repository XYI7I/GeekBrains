// See https://aka.ms/new-console-template for more information
Console.WriteLine("Задача 5*. Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает последнюю цифру этого числа.");

int num = 0;

while (num > 999 ^ num < 100)
{
    Console.Write("Введите трехзначное число: ");
    
    num  = int.Parse(Console.ReadLine ());
    
 }

string text = num.ToString(); 
char ltext = text[2];

Console.WriteLine("Последняя цифра трехзначного числа: " + num + " --> " + ltext);
