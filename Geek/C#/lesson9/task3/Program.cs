// 67. Напишите программу, которая будет принимать на вход число и возвращать сумму его цифр. 
Console.WriteLine("Программа принимает на вход число и возвращает сумму его цифр.");

Console.Write("Введите число: ");
int num = int.Parse(Console.ReadLine ());

void SumDigNum(int num, int sum = 0)
{
    if(num/10 == 0)
    {
        Console.WriteLine($"Сумма цифр = {sum + num}");
        return;
    }
    SumDigNum(num/10, sum + num%10);
}

SumDigNum(num);
