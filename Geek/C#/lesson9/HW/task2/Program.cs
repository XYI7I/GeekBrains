// 66. Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.
Console.WriteLine("Программа найдёт сумму натуральных элементов в промежутке от M до N");

Console.Write("Введите M промежутка от M до N: ");
int m = int.Parse(Console.ReadLine ());

Console.Write("Введите N промежутка от M до N: ");
int n = int.Parse(Console.ReadLine ());

int SumNumInt(int n, int m, int sum = 0)
{
    if(n == m) return n;       
    if (m < n) sum = n + SumNumInt(n-1, m);
    else sum = n + SumNumInt(n+1, m);
    return sum;
}

Console.WriteLine($"Сумма натуральных элементов в промежутке от {m} до {n} = {SumNumInt(n, m)}.");