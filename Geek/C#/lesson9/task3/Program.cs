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

int SumDigNumInt(int num)
{
    if(num/10 == 0) return num%10;
    num = num%10 + SumDigNumInt(num/10);
    return num;   
}

Console.WriteLine($"Сумма цифр чисдла {num} = {SumDigNumInt(num)}");
