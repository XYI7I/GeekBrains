// 18. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
Console.WriteLine("Программа, по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).");

int Input(int num_Q)
{
    while (num_Q <= 0 || num_Q > 4)
    {
        Console.Write("Ведите номер четверти, Q [1, 4]: ");
        num_Q = int.Parse(Console.ReadLine ());
    }
    return num_Q;
}

void Res_Q(int num_Q)
{
    string res = null;
    if (num_Q == 1 || num_Q == 4)
    {
        res = num_Q == 1? $"X > 0, Y > 0" : $"X > 0, Y < 0";
    }

    else
    {
        res = num_Q == 2? $"X < 0, Y > 0" : $"X < 0, Y < 0";
    }

    Console.WriteLine(res);
}

int Q = Input(0);
Res_Q(Q);