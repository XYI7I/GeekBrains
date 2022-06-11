// 70. Напишите программу, которая на вход принимает два числа и выдаёт первые N чисел, для которых каждое следующее равно сумме двух предыдущих. 
Console.WriteLine("Программа выведет первые N чисел, для которых каждое следующее равно сумме двух предыдущих.");

Console.Write("Введите первое число: ");
int a = int.Parse(Console.ReadLine ());

Console.Write("Введите второе число: ");
int b = int.Parse(Console.ReadLine ());

Console.Write("Введите количество чисел N: ");
int n = int.Parse(Console.ReadLine ());

if (b < a)
{
    int temp = b;
    b = a;
    a = temp;
}

void PrintSumNumInt(int a, int b, int n)
{
    if(n == 0) return; 
    Console.Write($"{a} ");
    int temp = b;
    b = a + b;
    a = temp;
    n--;
    PrintSumNumInt(a, b, n);
    return;
}


PrintSumNumInt(a, b, n);
Console.WriteLine();