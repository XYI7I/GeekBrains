// 28. Напишите программу, которая принимает на вход число (N) и выдает произведение чисел от 1 до N.
Console.WriteLine("Программа, которая принимает на вход число (N) и выдает произведение чисел от 1 до N");

Console.Write("Введите N: ");
int N = int.Parse(Console.ReadLine ());

void MultNum(int Num)
{
    int mult = 1;
    for (int i = 1; i <= N; i++)
    {
        mult = mult * i;

    }

    Console.WriteLine($"Произведение всех чисел от 1 до {N} = {mult}");
}

MultNum(N);
