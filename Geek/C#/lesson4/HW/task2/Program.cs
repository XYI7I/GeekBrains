// Задача 27: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе. 
Console.WriteLine("Программа принимает на вход число и выдаёт сумму цифр в числе.");

void SumDig()
{
    Console.Write("Введите число: ");
    int num = int.Parse(Console.ReadLine ());

    int sumdig = 0;
    for (int i = 1; i < num; i = i * 10)
    {
        sumdig += num % (i * 10) / i;
    }

    Console.WriteLine($"Сумма цифр в числе {num} -> {sumdig}");
}

SumDig();