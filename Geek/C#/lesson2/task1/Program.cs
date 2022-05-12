//  See https://aka.ms/new-console-template for more information
Console.WriteLine("9. Напишите программу, которая выводит случайное число из отрезка [10, 99] и показывает наибольшую цифру числа.");
Random rnd = new Random();
int num = rnd.Next(10, 99);

Console.WriteLine("Число = " + num);
if (num / 10 > num % 10)
{
    Console.WriteLine(num + " -> " + (num / 10));
}
else
{
    Console.WriteLine(num + " -> " + (num % 10));
}