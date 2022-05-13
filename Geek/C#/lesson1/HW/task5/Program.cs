// See https://aka.ms/new-console-template for more information
Console.WriteLine("Задача 5*. Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает последнюю цифру этого числа.");
int num = 0;
int absnum = 0;

while (absnum > 999 ^ absnum < 100)
{
    Console.Write("Введите трехзначное число: ");
    
    num  = int.Parse(Console.ReadLine ());
    absnum = Math.Abs(num);
    
 }

string text = num.ToString();
int length = text.Length - 1; 
char ltext = text[length];

Console.WriteLine("Последняя цифра трехзначного числа: " + num + " --> " + ltext);