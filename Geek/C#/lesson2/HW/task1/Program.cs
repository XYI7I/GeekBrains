// Задача 10: Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа. 
Console.WriteLine("Программа, принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа");

int num = 0;
int absnum = 0;

while (absnum > 999 ^ absnum < 100)
{
    Console.Write("Введите трехзначное число: ");
    
    num  = int.Parse(Console.ReadLine ());
    absnum = Math.Abs(num);
    
 }

 Console.WriteLine(num + " -> " + (absnum % 100) / 10);