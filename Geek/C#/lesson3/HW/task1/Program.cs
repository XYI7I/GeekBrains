// 19. Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
Console.WriteLine("Программа, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.");

int num = 0;

while (num > 99999 | num < 10000)
{
    Console.Write("Введите пятизначное число: ");    
    num  = int.Parse(Console.ReadLine ());       
}


void Palindrom_num(int num5)
{
    if (num5 / 10000 == num5 % 10 && num5 / 1000 % 10 == num5 % 100 / 10 )
    {
        Console.WriteLine(num5 + " -> да");
    }
    else
    {
        Console.WriteLine(num5 + " -> нет");
    }
}

void Palindrom_str(int num5)
{
    string text = num5.ToString();
    if (text[0] == text[4] && text[1] == text[3])
    {
        Console.WriteLine(num5 + " -> да");
    }
    else
    {
        Console.WriteLine(num5 + " -> нет");
    }
}

Palindrom_num(num);
Palindrom_str(num);