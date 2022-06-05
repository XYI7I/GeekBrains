// 69. Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
Console.WriteLine("Программа принимает два числа A и B, и возводит число А в целую степень B");

Console.Write("Введите число: ");
int num = int.Parse(Console.ReadLine ());
Console.Write("Введите степень: ");
int pow = int.Parse(Console.ReadLine ());

void PowNum(int num, int pow, int pownum = 1)
{   if(pow == 0)
    {
        Console.WriteLine($"{pownum} ");
        return;
    }
    pownum = pownum * num;
    pow--;
    PowNum(num, pow, pownum);
}

int PowNumInt(int num, int pow)
{   
    if (pow == 0) return 1;
    num = num * PowNumInt(num, --pow);
    return num;
}

Console.WriteLine($"Число {num} в степени {pow} = {PowNumInt(num, pow)}.");