// 45. Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.
Console.WriteLine("Программа считает, сколько чисел больше 0 ввёл пользователь.");

Console.Write("Введите количество M: ");
int m = int.Parse(Console.ReadLine ());

void PozNum(int m)
{
    int count = 0;
    for (int i = 0; i < m; i++)
    {
        Console.Write("Ведите число: ");
        int num = int.Parse(Console.ReadLine ());
        if (num > 0)
            count++;
    }
    Console.WriteLine($"Количество чисел больше 0: {count}");
}

PozNum (m);