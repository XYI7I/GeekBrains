// 63. Задайте значение N. Напишите программу, которая выведет все натуральные числа в промежутке от 1 до N.
Console.WriteLine("Программа выведет все натуральные числа в промежутке от 1 до N.");


Console.Write("Введите N промежутка от 1 до N: ");
int n = int.Parse(Console.ReadLine ());

void PrintNatNum(int n)
{
    if(n == 0)
        return;
    
    PrintNatNum(n-1);
    Console.Write($"{n} ");
}

PrintNatNum(n);