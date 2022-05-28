// 44. Не используя рекурсию, выведите первые N чисел Фибоначчи. Первые два числа Фибоначчи: 0 и 1.
Console.WriteLine("Программа выводить первые N чисел Фибоначчи.");

// N чисел Фибоначчи
int n = 0;
while (n < 2)
{
    Console.Write("Ведите число N: ");
    n = int.Parse(Console.ReadLine ());

}


void FibNum(int n)
{
    int[] fibarr = new int[n];
    fibarr [0] = 0;
    fibarr [1] = 1;
    for (int i = 2; i < n; i++)
    {
        fibarr[i] = fibarr[i - 1] + fibarr[i - 2];
    }
    var str = string.Join(" ", fibarr);
    Console.WriteLine($"Первые {n} чисел Фибоначчи: {str}");
}

FibNum(n);
