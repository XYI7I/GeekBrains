// 64. Задайте значения M и N. Напишите программу, которая выведет все натуральные числа в промежутке от M до N.
Console.WriteLine("Программа выведет все натуральные числа в промежутке от M до N.");

Console.Write("Введите M промежутка от M до N: ");
int m = int.Parse(Console.ReadLine ());

Console.Write("Введите N промежутка от M до N: ");
int n = int.Parse(Console.ReadLine ());

void PrintNatNumInt(int n, int m)
{
    if(n == m)
    {
        Console.Write($"{n} ");
        return;
    }       
    if (m < n)
    {        
        PrintNatNumInt(n-1, m);
        Console.Write($"{n} ");
    }
    else
    {
        PrintNatNumInt(n+1, m);
        Console.Write($"{n} ");        
    }    
}

PrintNatNumInt(n, m);
