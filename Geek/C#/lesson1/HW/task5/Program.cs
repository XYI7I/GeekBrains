﻿// See https://aka.ms/new-console-template for more information
Console.WriteLine("Задача 5*. Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает последнюю цифру этого числа.");

int num = 1000;

while (num > 999 ^ num < 100)
{
    Console.Write("Введите трехзначное число: ");
    
    num  = int.Parse(Console.ReadLine ());
    string text = num.ToString(); 
    text = text.Substring(2);
    
    Console.WriteLine(text);
}