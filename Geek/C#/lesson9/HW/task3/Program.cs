// 68. Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.
Console.WriteLine("Программа найдёт сумму натуральных элементов в промежутке от M до N");
int m = -1;
int n = -1;
while (m < 0 | n < 0)
{
    Console.Write("Введите положительное число m: ");
    m = int.Parse(Console.ReadLine ());

    Console.Write("Введите положительное число n: ");
    n = int.Parse(Console.ReadLine ());
}


int AkkermanFunc(int m, int n)
{
    if (m == 0) return n + 1;
    else if (m > 0 && n == 0)
        return AkkermanFunc(m - 1, 1);
    else
        return AkkermanFunc(m - 1, AkkermanFunc(m, n - 1));
}

Console.WriteLine(AkkermanFunc(m,n));
// Stack overflow if m >= 4!!!