// Задача 11: Напишите программу, которая выводит случайное трёхзначное число и удаляет вторую цифру этого числа.
Console.WriteLine("Программа, выводит случайное трёхзначное число и удаляет вторую цифру этого числа.");

Random rnd = new Random();
int num = rnd.Next(100, 1000);
Console.WriteLine("Число = " + num);

int num_dig2(int number)
{
    return (number / 100) * 10 + number % 10;
} 

Console.WriteLine("Модификация трехзначного числа: " + num + " -> " + num_dig2(num));
